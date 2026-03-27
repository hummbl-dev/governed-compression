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


if __name__ == "__main__":
    unittest.main()
