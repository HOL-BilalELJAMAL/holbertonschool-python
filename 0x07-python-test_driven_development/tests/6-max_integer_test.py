#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 6]), 6)
        self.assertEqual(max_integer([7, -23, 5, 18, 3]), 18)
        self.assertEqual(max_integer([-7, -23, -5, -18, -3]), -3)
        self.assertEqual(max_integer([70, 23, 5, 18, 3]), 70)
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5.87, 2.67, 14.91, 6.24]), 14.91)

    def test_errors(self):
        self.assertRaises(TypeError, max_integer, ['hello', '9', 4, 3])
        self.assertRaises(TypeError, max_integer, [[3, 4], True, (3, 8)])
