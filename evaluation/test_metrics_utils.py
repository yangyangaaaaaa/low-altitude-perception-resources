"""metrics_utils.py 的轻量回归测试，可用 python -m unittest evaluation.test_metrics_utils 运行。"""
import unittest

from evaluation.metrics_utils import (
    average_precision_binary,
    benchmark_fps,
    box_iou_2d,
    box_iou_3d_axis_aligned,
    confusion_matrix,
    mean_absolute_error,
    metrics_from_confusion,
    relative_gain,
    segmentation_metrics,
    success_rate,
    success_weighted_by_path_length,
    threshold_accuracy,
    count_parameters,
)


class MetricTests(unittest.TestCase):
    def test_segmentation_metrics_and_ignore_index(self):
        report = segmentation_metrics([0, 0, 1, 1, 255], [0, 1, 1, 1, 0], 2, 255)
        self.assertEqual(report["confusion_matrix"], [[1, 1], [0, 2]])
        self.assertAlmostEqual(report["OA"], 0.75)
        self.assertAlmostEqual(report["mIoU"], 7 / 12)
        self.assertAlmostEqual(report["mean_DSC"], 11 / 15)

    def test_box_iou(self):
        self.assertAlmostEqual(box_iou_2d((0, 0, 2, 2), (1, 1, 3, 3)), 1 / 7)
        self.assertAlmostEqual(
            box_iou_3d_axis_aligned((0, 0, 0, 2, 2, 2), (1, 1, 1, 3, 3, 3)),
            1 / 15,
        )
        self.assertEqual(box_iou_2d((0, 0, 1, 1), (2, 2, 3, 3)), 0.0)

    def test_binary_ap(self):
        self.assertAlmostEqual(average_precision_binary([0.9, 0.8, 0.7], [1, 0, 1]), 5 / 6)

    def test_threshold_and_success_rates(self):
        self.assertAlmostEqual(threshold_accuracy([0.5, 0.6], 0.6), 0.5)
        self.assertAlmostEqual(success_rate([0.4, 0.6, 0.8]), 2 / 3)
        self.assertAlmostEqual(success_weighted_by_path_length([1, 0], [10, 20], [12, 20]), 5 / 12)

    def test_mae_and_relative_gain(self):
        self.assertAlmostEqual(mean_absolute_error([1, 2, 3], [1, 3, 2]), 2 / 3)
        self.assertAlmostEqual(relative_gain(1.2, 1.0), 0.2)

    def test_fps_helper(self):
        report = benchmark_fps(lambda: sum(range(10)), warmup=1, repeats=3)
        self.assertGreater(report["mean_latency_ms"], 0)
        self.assertGreater(report["throughput_fps"], 0)

    def test_parameter_counter(self):
        class Parameter:
            def __init__(self, size, trainable):
                self.size = size
                self.requires_grad = trainable
            def numel(self):
                return self.size
        class Model:
            def parameters(self):
                return [Parameter(3, True), Parameter(5, False)]
        self.assertEqual(count_parameters(Model()), 8)
        self.assertEqual(count_parameters(Model(), trainable_only=True), 3)

    def test_invalid_inputs_raise(self):
        with self.assertRaises(ValueError):
            confusion_matrix([0, 1], [0], 2)
        with self.assertRaises(ValueError):
            average_precision_binary([0.5], [0])
        with self.assertRaises(ValueError):
            box_iou_2d((0, 0, 1), (0, 0, 1, 1))


if __name__ == "__main__":
    unittest.main()
