import unittest
from utils import arrs


class TestArrs(unittest.TestCase):
    def setUp(self):
        self.array = [1, 2, 3, 4]

    def test_get(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, "test"), "test")
        self.assertEqual(arrs.get([1, 2, 3], -1, None), None)

    def test_slice(self):
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], 1, 3), [2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3], 1), [2, 3])
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -5, 2), [1, 2])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4], -3, 3), [2, 3])
