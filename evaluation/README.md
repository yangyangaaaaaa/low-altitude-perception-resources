# 低空视觉评价指标与代码入口

本目录参考图像融合项目将评测代码独立成目录的组织方式，提供常见低空视觉指标的代码入口、评测协议和基础 Python 辅助实现。主页也直接展示全部评价指标，方便浏览者无需下载即可查找。

## 快速运行

在项目根目录执行：

```bash
python evaluation/metrics_utils.py
python -m unittest evaluation.test_metrics_utils
```

第一条命令运行示例；第二条命令运行本包附带的 8 项回归测试。示例不依赖第三方库，覆盖混淆矩阵、OA、mAcc、mIoU、DSC、二维/三维轴对齐框 IoU、基础二分类 AP、MAE、阈值准确率、跟踪成功率和 SPL。

可在自己的 Python 程序中导入：

```python
from evaluation.metrics_utils import (
    segmentation_metrics, box_iou_2d, box_iou_3d_axis_aligned,
    average_precision_binary, mean_absolute_error, threshold_accuracy,
    success_rate, success_weighted_by_path_length, benchmark_fps,
    count_parameters, count_flops_fvcore, relative_gain,
)

truth = [0, 0, 1, 1]
prediction = [0, 1, 1, 1]
print(segmentation_metrics(truth, prediction, num_classes=2)["mIoU"])
print(box_iou_2d((0, 0, 2, 2), (1, 1, 3, 3)))
```

## 指标与代码入口

以下按任务拆分，便于从主页或本目录快速查找。公开框架链接用于正式基准计算；本包实现标有“本包代码”。
### 目标检测与精确率/召回率

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| Precision | 精确率，预测为正的样本中真正例所占比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html) | [`metrics_utils.py`](metrics_utils.py) |
| Recall | 召回率，真实正样本中被正确检出的比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html) | [`metrics_utils.py`](metrics_utils.py) |
| AP | 平均精度，Precision—Recall曲线下的面积。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | [`metrics_utils.py`](metrics_utils.py) |
| mAP | 各类别AP的平均值。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| AP50 | IoU阈值为0.50时的平均精度。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| AP75 | IoU阈值为0.75时的平均精度。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APS | 小目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APM | 中等目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |
| APL | 大目标区域上的AP。 | [代码/项目](https://github.com/cocodataset/cocoapi) | [协议/文档](https://cocodataset.org/#detection-eval) | — |

### 语义分割与像素分类

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| IoU | 预测区域或检测框与真值的交集除以并集。 | [代码/项目](https://github.com/Lightning-AI/torchmetrics) | [协议/文档](https://torchmetrics.readthedocs.io/en/stable/classification/jaccard_index.html) | [`metrics_utils.py`](metrics_utils.py) |
| DSC | Dice相似系数，按两倍交集除以预测区域与真值区域面积之和计算。 | [代码/项目](https://github.com/Lightning-AI/torchmetrics) | [协议/文档](https://lightning.ai/docs/torchmetrics/stable/segmentation/dice.html) | [`metrics_utils.py`](metrics_utils.py) |
| mIoU | 各类别IoU的平均值。 | [代码/项目](https://github.com/open-mmlab/mmsegmentation) | [协议/文档](https://mmsegmentation.readthedocs.io/en/latest/) | [`metrics_utils.py`](metrics_utils.py) |
| OA | 整体精度，所有正确分类像素或样本占总数的比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | [`metrics_utils.py`](metrics_utils.py) |
| Acc | 准确率，按具体任务定义的正确预测比例。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html) | [`metrics_utils.py`](metrics_utils.py) |
| mAcc | 各类别准确率或召回率的平均值，具体沿用基准定义。 | [代码/项目](https://github.com/open-mmlab/mmsegmentation) | [协议/文档](https://mmsegmentation.readthedocs.io/en/latest/) | [`metrics_utils.py`](metrics_utils.py) |

### 三维检测、深度与距离

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| 3D IoU | 三维检测框与三维真值框在空间中的交并比。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | [`metrics_utils.py`](metrics_utils.py) |
| AP3D | 基于三维空间IoU计算的平均精度。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | — |
| APBEV | 将三维框投影到鸟瞰图后计算IoU得到的平均精度。 | [代码/项目](https://github.com/open-mmlab/mmdetection3d) | [协议/文档](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/evaluation.html) | — |
| MAE | 预测值与真值绝对误差的平均值。 | [代码/项目](https://github.com/scikit-learn/scikit-learn) | [协议/文档](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html) | [`metrics_utils.py`](metrics_utils.py) |
| <0.6m accuracy | 误差或定位偏差小于0.6 m的样本比例。 | — | — | [`metrics_utils.py`](metrics_utils.py) |

### 跟踪与无人机导航

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| Success | 跟踪结果与真值的重叠度达到不同阈值时形成的成功率曲线或其汇总值。 | [代码/项目](https://github.com/visionml/pytracking) | [协议/文档](https://github.com/visionml/pytracking) | [`metrics_utils.py`](metrics_utils.py) |
| SR | 导航任务成功率，按目标到达或任务完成条件统计，定义依具体基准。 | [代码/项目](https://github.com/facebookresearch/habitat-lab) | [协议/文档](https://aihabitat.org/challenge/) | [`metrics_utils.py`](metrics_utils.py) |
| SPL | 路径长度加权成功率，综合任务成功与实际路径效率。 | [代码/项目](https://github.com/facebookresearch/habitat-lab) | [协议/文档](https://aihabitat.org/challenge/) | [`metrics_utils.py`](metrics_utils.py) |
| MOTA | 综合漏检、误检和身份切换的多目标跟踪准确率。 | [代码/项目](https://github.com/JonathonLuiten/TrackEval) | [协议/文档](https://motchallenge.net/results/MOT17/) | — |
| IDF1 | 身份一致性F1分数，衡量轨迹身份匹配质量。 | [代码/项目](https://github.com/JonathonLuiten/TrackEval) | [协议/文档](https://motchallenge.net/results/MOT17/) | — |

### 模型效率与对比统计

| 指标 | 说明 | 代码/项目 | 评测协议 | 本包代码 |
| :--- | :--- | :--- | :--- | :--- |
| 参数量 | 模型可训练或可推理参数的数量。 | [代码/项目](https://github.com/TylerYep/torchinfo) | [协议/文档](https://github.com/TylerYep/torchinfo) | [`metrics_utils.py`](metrics_utils.py) |
| FLOPs | 给定输入形状下的浮点运算量估计。 | [代码/项目](https://github.com/facebookresearch/fvcore) | [协议/文档](https://github.com/facebookresearch/fvcore) | [`metrics_utils.py`](metrics_utils.py) |
| FPS | 单位时间处理的图像或视频帧数。 | — | [协议/文档](https://docs.pytorch.org/docs/stable/benchmark_utils.html) | [`metrics_utils.py`](metrics_utils.py) |
| 增益 | 相对于基线或对照模型的指标变化量或相对提升比例。 | — | — | [`metrics_utils.py`](metrics_utils.py) |

## 使用说明

- `average_precision_binary` 是便于理解的基础二分类 AP 示例，不替代 COCO 等目标检测基准的 AP/mAP 评测。
- `box_iou_2d` 与 `box_iou_3d_axis_aligned` 仅计算轴对齐框 IoU；旋转框、BEV/AP3D 及数据集官方结果请使用相应基准代码。
- 分割指标按混淆矩阵计算；类别缺失时，宏平均仅纳入真值中出现的类别。类别编号和忽略标签应与数据集协议一致。
- `threshold_accuracy` 使用严格小于阈值的条件，适用于 `<0.6m accuracy` 这类写法。
- `success_rate` 是单一重叠阈值下的基础成功率示例，不等同于所有跟踪基准的成功率曲线或曲线下面积。
- FPS、参数量与 FLOPs 会随输入尺寸、算子覆盖、硬件和测量设置变化；正式比较应以论文或基准给出的协议为准。

## 文件

- [`metrics_utils.py`](metrics_utils.py)：本包编写的通用指标与效率统计辅助函数；
- [`test_metrics_utils.py`](test_metrics_utils.py)：8 项可直接运行的回归测试；
- [`../metrics_open_resources.csv`](../metrics_open_resources.csv)：评价指标分类、公开实现、协议入口和说明。
