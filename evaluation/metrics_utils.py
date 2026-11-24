"""常用低空视觉评价指标的基础实现。

任务级 AP、三维检测和多目标跟踪应使用对应数据集/挑战赛的官方评测协议。
本文件提供通用分类/分割、轴对齐框 IoU、二分类基础 AP、MAE、阈值准确率、跟踪成功率、SPL、FPS 与参数量辅助函数。AP、旋转框/三维检测及挑战赛指标应使用对应官方评测器。
"""

from __future__ import annotations

from statistics import mean, median
import sys
from time import perf_counter
from typing import Any, Callable, Iterable, Optional, Sequence


def _flat(values: Any) -> list[Any]:
    """展平 Python 序列、NumPy 数组或 Torch 张量。"""
    if hasattr(values, "detach"):
        values = values.detach().cpu()
    if hasattr(values, "reshape") and hasattr(values, "tolist"):
        values = values.reshape(-1).tolist()
    result: list[Any] = []

    def visit(item: Any) -> None:
        if isinstance(item, (list, tuple)):
            for part in item:
                visit(part)
        else:
            result.append(item)

    visit(values)
    return result


def confusion_matrix(
    y_true: Any,
    y_pred: Any,
    num_classes: int,
    ignore_index: Optional[int] = None,
) -> list[list[int]]:
    """返回混淆矩阵，行是真值类别，列是预测类别。"""
    if num_classes <= 0:
        raise ValueError("num_classes 必须为正整数")
    truth = _flat(y_true)
    pred = _flat(y_pred)
    if len(truth) != len(pred):
        raise ValueError("y_true 与 y_pred 的元素数量必须一致")

    matrix = [[0 for _ in range(num_classes)] for _ in range(num_classes)]
    for t, p in zip(truth, pred):
        t, p = int(t), int(p)
        if ignore_index is not None and t == ignore_index:
            continue
        if not 0 <= t < num_classes or not 0 <= p < num_classes:
            raise ValueError(f"类别索引超出范围：真值={t}, 预测={p}")
        matrix[t][p] += 1
    return matrix


def metrics_from_confusion(
    matrix: Sequence[Sequence[int]],
) -> dict[str, Any]:
    """从混淆矩阵计算 OA、mAcc、mIoU、Dice 及逐类 Precision/Recall/IoU/Dice。"""
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("混淆矩阵必须为非空方阵")

    total = sum(sum(int(v) for v in row) for row in matrix)
    if total == 0:
        raise ValueError("混淆矩阵没有有效样本")

    per_class = []
    recalls = []
    ious = []
    dices = []
    for c in range(n):
        tp = int(matrix[c][c])
        fp = sum(int(matrix[r][c]) for r in range(n) if r != c)
        fn = sum(int(matrix[c][k]) for k in range(n) if k != c)
        support = tp + fn
        pred_count = tp + fp
        union = tp + fp + fn
        precision = tp / pred_count if pred_count else None
        recall = tp / support if support else None
        iou = tp / union if union else None
        dice_denominator = 2 * tp + fp + fn
        dice = 2 * tp / dice_denominator if dice_denominator else None
        if recall is not None:
            recalls.append(recall)
        if iou is not None:
            ious.append(iou)
        if dice is not None:
            dices.append(dice)
        per_class.append({
            "class_index": c,
            "support": support,
            "precision": precision,
            "recall": recall,
            "iou": iou,
            "dice": dice,
        })

    return {
        "OA": sum(int(matrix[c][c]) for c in range(n)) / total,
        "mAcc": mean(recalls) if recalls else None,
        "mIoU": mean(ious) if ious else None,
        "mean_DSC": mean(dices) if dices else None,
        "per_class": per_class,
    }


def segmentation_metrics(
    y_true: Any,
    y_pred: Any,
    num_classes: int,
    ignore_index: Optional[int] = None,
) -> dict[str, Any]:
    """计算多类别语义分割常见指标。输入为类别索引图或可展平序列。"""
    matrix = confusion_matrix(y_true, y_pred, num_classes, ignore_index)
    result = metrics_from_confusion(matrix)
    result["confusion_matrix"] = matrix
    return result


def box_iou_2d(box_a: Sequence[float], box_b: Sequence[float]) -> float:
    """计算轴对齐二维框的 IoU。框格式为 (x1, y1, x2, y2)。"""
    if len(box_a) != 4 or len(box_b) != 4:
        raise ValueError("二维框必须包含 x1、y1、x2、y2")
    ax1, ay1, ax2, ay2 = (float(v) for v in box_a)
    bx1, by1, bx2, by2 = (float(v) for v in box_b)
    if ax2 < ax1 or ay2 < ay1 or bx2 < bx1 or by2 < by1:
        raise ValueError("框的右下角坐标不能小于左上角坐标")
    inter_w = max(0.0, min(ax2, bx2) - max(ax1, bx1))
    inter_h = max(0.0, min(ay2, by2) - max(ay1, by1))
    intersection = inter_w * inter_h
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    union = area_a + area_b - intersection
    return intersection / union if union > 0 else 0.0


def box_iou_3d_axis_aligned(
    box_a: Sequence[float], box_b: Sequence[float]
) -> float:
    """计算轴对齐三维框的 IoU；框格式为 (x1, y1, z1, x2, y2, z2)。"""
    if len(box_a) != 6 or len(box_b) != 6:
        raise ValueError("三维框必须包含 x1、y1、z1、x2、y2、z2")
    a = tuple(float(v) for v in box_a)
    b = tuple(float(v) for v in box_b)
    if any(a[i + 3] < a[i] or b[i + 3] < b[i] for i in range(3)):
        raise ValueError("框的右上后角坐标不能小于左下前角坐标")
    intersection = 1.0
    for i in range(3):
        intersection *= max(0.0, min(a[i + 3], b[i + 3]) - max(a[i], b[i]))
    volume_a = (a[3] - a[0]) * (a[4] - a[1]) * (a[5] - a[2])
    volume_b = (b[3] - b[0]) * (b[4] - b[1]) * (b[5] - b[2])
    union = volume_a + volume_b - intersection
    return intersection / union if union > 0 else 0.0


def average_precision_binary(scores: Any, labels: Any) -> float:
    """按全点插值计算二分类 AP；正式检测结果应使用数据集官方评测器。"""
    score_values = [float(v) for v in _flat(scores)]
    label_values = [1 if int(v) else 0 for v in _flat(labels)]
    if len(score_values) != len(label_values) or not score_values:
        raise ValueError("scores 与 labels 必须为长度相同的非空序列")
    if sum(label_values) == 0:
        raise ValueError("AP 至少需要一个正样本")
    order = sorted(range(len(score_values)), key=lambda i: score_values[i], reverse=True)
    tp = 0
    fp = 0
    precisions = []
    recalls = []
    positives = sum(label_values)
    for index in order:
        if label_values[index]:
            tp += 1
        else:
            fp += 1
        precisions.append(tp / (tp + fp))
        recalls.append(tp / positives)
    recall_points = [0.0] + recalls + [1.0]
    precision_points = [0.0] + precisions + [0.0]
    for index in range(len(precision_points) - 1, 0, -1):
        precision_points[index - 1] = max(
            precision_points[index - 1], precision_points[index]
        )
    return sum(
        (recall_points[index + 1] - recall_points[index]) * precision_points[index + 1]
        for index in range(len(recall_points) - 1)
    )


def success_rate(overlaps: Any, threshold: float = 0.5) -> float:
    """按重叠度阈值计算基础跟踪成功率。"""
    values = [float(v) for v in _flat(overlaps)]
    if not values or not 0.0 <= threshold <= 1.0:
        raise ValueError("overlaps 不能为空且 threshold 必须位于 [0, 1]")
    return sum(value >= threshold for value in values) / len(values)

def mean_absolute_error(y_true: Any, y_pred: Any) -> float:
    """计算平均绝对误差（MAE）。"""
    truth = [float(v) for v in _flat(y_true)]
    pred = [float(v) for v in _flat(y_pred)]
    if len(truth) != len(pred) or not truth:
        raise ValueError("MAE 输入必须为长度相同的非空序列")
    return sum(abs(t - p) for t, p in zip(truth, pred)) / len(truth)


def success_weighted_by_path_length(
    success: Iterable[float],
    shortest_path_lengths: Iterable[float],
    actual_path_lengths: Iterable[float],
) -> float:
    """计算 SPL；每个 episode 的成功值通常为 0 或 1。"""
    success = [float(v) for v in success]
    shortest = [float(v) for v in shortest_path_lengths]
    actual = [float(v) for v in actual_path_lengths]
    if not success or not (len(success) == len(shortest) == len(actual)):
        raise ValueError("SPL 三个输入必须为长度相同的非空序列")
    if any(v < 0 for v in shortest + actual):
        raise ValueError("路径长度不能为负数")
    scores = []
    for s, optimal, travelled in zip(success, shortest, actual):
        if not 0.0 <= s <= 1.0:
            raise ValueError("success 值必须位于 [0, 1]")
        denominator = max(optimal, travelled)
        ratio = optimal / denominator if denominator > 0 else 0.0
        scores.append(s * ratio)
    return mean(scores)



def threshold_accuracy(errors: Any, threshold: float) -> float:
    """计算绝对误差严格小于给定阈值的样本比例。"""
    values = [abs(float(v)) for v in _flat(errors)]
    if not values or threshold < 0:
        raise ValueError("errors 不能为空且 threshold 不能为负数")
    return sum(v < threshold for v in values) / len(values)


def relative_gain(value: float, baseline: float) -> float:
    """计算相对基线的百分比变化；返回值为小数形式。"""
    value, baseline = float(value), float(baseline)
    if baseline == 0:
        raise ValueError("baseline 不能为 0")
    return (value - baseline) / abs(baseline)


def benchmark_fps(
    predict: Callable[[], Any],
    warmup: int = 10,
    repeats: int = 100,
    items_per_call: int = 1,
    synchronize: Optional[Callable[[], Any]] = None,
) -> dict[str, float]:
    """测量单进程推理吞吐量；GPU 测试需传入同步函数以等待异步计算完成。"""
    if warmup < 0 or repeats <= 0 or items_per_call <= 0:
        raise ValueError("warmup、repeats、items_per_call 设置不合法")

    def sync() -> None:
        if synchronize is not None:
            synchronize()

    for _ in range(warmup):
        predict()
    sync()

    durations = []
    for _ in range(repeats):
        sync()
        start = perf_counter()
        predict()
        sync()
        durations.append(perf_counter() - start)

    total_time = sum(durations)
    return {
        "mean_latency_ms": mean(durations) * 1000.0,
        "median_latency_ms": median(durations) * 1000.0,
        "throughput_fps": items_per_call * repeats / total_time if total_time else float("inf"),
    }


def count_parameters(model: Any, trainable_only: bool = False) -> int:
    """统计 PyTorch 模型参数量；默认统计全部参数。"""
    try:
        parameters = model.parameters()
    except AttributeError as exc:
        raise TypeError("model 应为具有 parameters() 方法的 PyTorch 模型") from exc
    return sum(
        int(parameter.numel())
        for parameter in parameters
        if not trainable_only or bool(getattr(parameter, "requires_grad", False))
    )


def count_flops_fvcore(model: Any, inputs: tuple[Any, ...]) -> float:
    """使用 fvcore 统计给定输入下的 FLOPs；具体算子覆盖范围见 fvcore 文档。"""
    try:
        from fvcore.nn import FlopCountAnalysis
    except ImportError as exc:
        raise ImportError("请安装 fvcore：pip install fvcore") from exc
    return float(FlopCountAnalysis(model, inputs).total())


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    truth = [0, 0, 1, 1]
    prediction = [0, 1, 1, 1]
    report = segmentation_metrics(truth, prediction, num_classes=2)
    print("混淆矩阵：", report["confusion_matrix"])
    print("OA={:.4f} mAcc={:.4f} mIoU={:.4f} DSC={:.4f}".format(
        report["OA"], report["mAcc"], report["mIoU"], report["mean_DSC"]
    ))
    print("MAE 示例：", mean_absolute_error([1, 2, 3], [1, 3, 2]))
    print("SPL 示例：", success_weighted_by_path_length(
        [1, 0], [10, 20], [12, 20]
    ))
    print("二维框 IoU 示例：", box_iou_2d((0, 0, 2, 2), (1, 1, 3, 3)))
    print("三维轴对齐框 IoU 示例：", box_iou_3d_axis_aligned(
        (0, 0, 0, 2, 2, 2), (1, 1, 1, 3, 3, 3)
    ))
    print("基础二分类 AP 示例：", average_precision_binary(
        [0.9, 0.8, 0.7], [1, 0, 1]
    ))
    print("跟踪成功率示例：", success_rate([0.4, 0.6, 0.8]))
