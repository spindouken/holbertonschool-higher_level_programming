#!/usr/bin/python3
"""
Based unittest for Rectangle class
run with python3 -m unittest tests/test_models/test_rectangle.py
or run with run all tests command:
    python3 -m unittest discover tests
OR just run it like a program! (thanks to bottom function)
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testDatRectangle(unittest.TestCase):
    def test_init_given_values(self):
        """test if attributes are correctly initialized"""
        r = Rectangle(3, 4, 6, 7, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_init_default_values(self):
        """test that init method assigns default values when none are provided"""
        r = Rectangle(3, 4)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)
    
    def test_init_id_none(self):
        """test that __nb_object increments and assigns id
            properly when none provided"""
        r1 = Rectangle(3, 4)
        r2 = Rectangle(3, 4)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 3)
        
    # test setters
    def test_width_setter(self):
        """test that width setter method updates width correctly"""
        r = Rectangle(3, 4, 0, 0, 1)
        r.width = 5
        self.assertEqual(r.width, 5)
    
    def test_height_setter(self):
        """test that height setter method updates height correctly"""
        r = Rectangle(3, 4, 0, 0, 1)
        r.height = 5
        self.assertEqual(r.height, 5)
        
    def test_x_setter(self):
        """test x coordinate setter method updates x coordinate correctly"""
        r = Rectangle(3, 4, 0, 0, 1)
        r.x = 5
        self.assertEqual(r.x, 5)
        
    def test_y_setter(self):
        """Test y coordinate setter method updates y coordinate correctly"""
        r = Rectangle(3, 4, 0, 0, 1)
        r.y = 5
        self.assertEqual(r.y, 5)

if __name__ == '__main__':
    unittest.main()
