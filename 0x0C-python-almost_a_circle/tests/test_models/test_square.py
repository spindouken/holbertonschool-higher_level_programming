#!/usr/bin/python3
"""
Based unittest for Rectangle class
run with python3 -m unittest tests/test_models/test_square.py
    or run with run all tests command:
        "python3 -m unittest discover tests"
    OR just run it like a program! (thanks to bottom function)
"""
import unittest
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_init(self):
        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 3)
        self.assertEqual(s1.id, 4)

    def test_update(self):
        s1 = Square(2, 3, 4, 5)
        s1.update(5)
        self.assertEqual(s1.id, 5)
        s1.update(size=10)
        self.assertEqual(s1.size, 10)

    def test_to_dictionary(self):
        s1 = Square(4, 1, 2, 3)
        dic = s1.to_dictionary()
        self.assertEqual(dic, {'id': 3, 'x': 1, 'size': 4, 'y': 2})

    def test_str(self):
        s1 = Square(4, 3, 2, 1)
        s = str(s1)
        self.assertEqual(s, "[Square] (1) 3/2 - 4")

if __name__ == '__main__':
    unittest.main()
