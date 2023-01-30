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
    def test_invalid_args_amount(self):
        """tests for too many args"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6, 7)
        """tests for too little args"""
        with self.assertRaises(TypeError):
            Rectangle(1)
            Rectangle()
            Rectangle(None)

    def test_private_attr_access(self):
        """tests that private attributes are not accessible"""
        with self.assertRaises(AttributeError):
            print(Rectangle.__width)
            print(Rectangle.__height)
            print(Rectangle.__x)
            print(Rectangle.__y)

    def test_init_given_values(self):
        """test if attributes are correctly initialized"""
        r = Rectangle(3, 4, 6, 7, 1)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 6)
        self.assertEqual(r.y, 7)
        self.assertEqual(r.id, 1)

    def test_init_default_values(self):
        """test init method assigns default values when none are provided"""
        r = Rectangle(2, 3)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertTrue(r.id is not None)

    def test_init_id_none(self):
        """test that __nb_object increments and assigns id
            properly when none provided"""
        r1 = Rectangle(3, 4)
        r2 = Rectangle(3, 4)
        self.assertTrue(r1.id is not None)
        self.assertTrue(r2.id is not None)

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
        """test y coordinate setter method updates y coordinate correctly"""
        r = Rectangle(3, 4, 0, 0, 1)
        r.y = 5
        self.assertEqual(r.y, 5)

    # test with string input
    def test_width_with_string(self):
        """tests width with string input"""
        with self.assertRaises(TypeError):
            r = Rectangle("5", 4, 0, 0, 1)

    def test_height_type(self):
        """tests height with string input"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, "4", 0, 0, 1)

    def test_x_type(self):
        """tests x with string input"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, "0", 0, 1)

    def test_y_type(self):
        """tests y with string input"""
        with self.assertRaises(TypeError):
            r = Rectangle(5, 4, 0, "0", 1)

    # value greater than zero check
    def test_width_greater_than_zero(self):
        """tests that width is greater than 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(-5, 4, 0, 0, 1)

    def test_height_value(self):
        """tests that height is greater than 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, -4, 0, 0, 1)

    def test_x_value(self):
        """tests that x is greater than or equal to 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 4, -1, 0, 1)

    def test_y_value(self):
        """tests that y is greater than or equal to 0"""
        with self.assertRaises(ValueError):
            r = Rectangle(5, 4, 0, -1, 1)

    # test rectangle area function
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_area_decimal(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(2.5, 3.5)

    def test_area_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-2, -3)

    def test_area_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 0)

    # check str override
    def test_str_override(self):
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_str_override_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-10, -20, -30, -40, -50)

    def test_str_override_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 0, 0, 0, 0)

    # check update function
    def setUp(self):
        self.r = Rectangle(1, 2, 3, 4, 5)

    def test_update_id(self):
        self.r.update(6)
        self.assertEqual(self.r.id, 6)

    def test_update_width(self):
        self.r.update(1, 7)
        self.assertEqual(self.r.width, 7)

    def test_update_height(self):
        self.r.update(1, 2, 8)
        self.assertEqual(self.r.height, 8)

    def test_update_x(self):
        self.r.update(1, 2, 3, 9)
        self.assertEqual(self.r.x, 9)

    def test_update_y(self):
        self.r.update(1, 2, 3, 4, 10)
        self.assertEqual(self.r.y, 10)

    def test_update_all(self):
        self.r.update(11, 12, 13, 14, 15)
        self.assertEqual(self.r.id, 11)
        self.assertEqual(self.r.width, 12)
        self.assertEqual(self.r.height, 13)
        self.assertEqual(self.r.x, 14)
        self.assertEqual(self.r.y, 15)

    # dictionary tests
    def test_to_dictionary(self):
        r = Rectangle(10, 10, 2, 1, 9)
        expected = {'x': 2, 'y': 1, 'id': 9, 'height': 10, 'width': 10}
        self.assertEqual(r.to_dictionary(), expected)

if __name__ == '__main__':
    unittest.main()
