from __future__ import annotations

import unittest

import numpy as np

from governed_compression.core.config import CompressionConfig
from governed_compression.core.reference import approximate_dot, quantize_reference


class ReferenceTests(unittest.TestCase):
    def test_quantize_reference_preserves_shape(self) -> None:
        vector = np.array([0.1, 0.4, 0.7], dtype=np.float32)
        config = CompressionConfig(method="scalar_baseline", bits_per_channel=4.0)
        result = quantize_reference(vector, config)
        self.assertEqual(result.shape, vector.shape)

    def test_approximate_dot_returns_float(self) -> None:
        left = np.array([1.0, 2.0], dtype=np.float32)
        right = np.array([3.0, 4.0], dtype=np.float32)
        result = approximate_dot(left, right)
        self.assertIsInstance(result, float)
        self.assertEqual(result, 11.0)

    def test_quantize_uniform_vector_returns_zeros(self) -> None:
        vector = np.full(5, 3.14, dtype=np.float32)
        config = CompressionConfig(method="scalar_baseline", bits_per_channel=8.0)
        result = quantize_reference(vector, config)
        np.testing.assert_array_equal(result, np.zeros(5, dtype=np.float32))

    def test_quantize_output_range(self) -> None:
        rng = np.random.default_rng(42)
        vector = rng.standard_normal(256).astype(np.float32)
        config = CompressionConfig(method="scalar_baseline", bits_per_channel=4.0)
        result = quantize_reference(vector, config)
        self.assertGreaterEqual(float(result.min()), 0.0)
        self.assertLessEqual(float(result.max()), 1.0)

    def test_mse_zero_for_identical(self) -> None:
        from governed_compression.bench.distortion import mean_squared_error
        a = np.array([1.0, 2.0, 3.0], dtype=np.float32)
        self.assertEqual(mean_squared_error(a, a), 0.0)

    def test_mse_positive_for_distinct(self) -> None:
        from governed_compression.bench.distortion import mean_squared_error
        a = np.array([1.0, 2.0, 3.0], dtype=np.float32)
        b = np.array([1.5, 2.5, 3.5], dtype=np.float32)
        self.assertGreater(mean_squared_error(a, b), 0.0)


if __name__ == "__main__":
    unittest.main()
