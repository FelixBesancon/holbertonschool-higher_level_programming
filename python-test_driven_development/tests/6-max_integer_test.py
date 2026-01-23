#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for max_integer"""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 9, 2, 3]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_negative_positive(self):
        self.assertEqual(max_integer([-10, 0, 10, 5]), 10)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_mixed_types_raises(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
