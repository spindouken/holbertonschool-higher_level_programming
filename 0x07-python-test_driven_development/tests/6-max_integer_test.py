#!/usr/bin/python3
"""Unit tests for def max_integer(list=[])"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_int_list(self):
        self.assertEqual(max_integer([9, 4, 7]), 9)
        self.assertEqual(max_integer([6, 5, 2]), 6)
        self.assertEqual(max_integer([9, 3, 5]), 9)
        self.assertEqual(max_integer([4]), 4)

    def test_negative_int_list(self):
        self.assertEqual(max_integer([-9, -4, -7]), -4)
        self.assertEqual(max_integer([-6, -5, -2]), -2)
        self.assertEqual(max_integer([-9, -3, -5]), -3)
        self.assertEqual(max_integer([-4]), -4)

    def test_neg_and_pos_int_list(self):
        self.assertEqual(max_integer([-9, 4, -7]), 4)
        self.assertEqual(max_integer([-6, 5, 2]), 5)
        self.assertEqual(max_integer([-9, -3, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_floats_in_list(self):
        self.assertEqual(max_integer([1.2, 4.7, 9.9]), 9.9)
        self.assertEqual(max_integer([9000, 5.6, 9000.1]), 9000.1)
        self.assertEqual(max_integer([2.6, 8.4, 6.7]), 8.4)

    def test_string_list(self):
        self.assertEqual(max_integer("Hello??"), 'o')
        self.assertEqual(max_integer(["Is this thing", "on?"]), "on?")
        self.assertEqual(max_integer(""), None)
