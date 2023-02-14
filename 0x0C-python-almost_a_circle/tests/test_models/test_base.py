#!/usr/bin/python3
"""
Based unittest for Base class
run with python3 -m unittest tests/test_models/test_base.py
    or run with run all tests command:
        "python3 -m unittest discover tests"
    OR just run it like a program! (thanks to bottom function)
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testIfBased(unittest.TestCase):
    def test_id_assignment(self):
        """serves same purpose as if __nb_objects starts at 0
            and increments by 1"""
        base1 = Base(1)
        base2 = Base(2)
        self.assertEqual(base1.id, base2.id - 1)

    def test_id_none(self):
        """testing if Base id assigned as None will still be incremented"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, base2.id - 1)

    def test_no_args(self):
        """leave Base id assignment blank
        each base object should be automatically assigned an id"""
        base5 = Base()
        base6 = Base()
        base7 = Base()
        base8 = Base()
        self.assertEqual(base5.id, base8.id - 3)

    def test_id_uniq(self):
        self.assertEqual(5, Base(5).id)
    
    def test_id_pub(self):
        base1 = Base(0)
        base1.id = 5
        self.assertEqual(5, base1.id)

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_dict(self):
        self.assertEqual(str, type(Base.to_json_string([{'id': 12}])))

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_dict(self):
        self.assertEqual(list, type(Base.from_json_string('[{"id": 89}]')))

class testIfBasedSave(unittest.TestCase):
    @classmethod
    def cleanUp(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_re(self):
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as f:
            self.assertTrue(len(f.read()) == 53)

    def test_save_to_file_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_sq(self):
        sq = Square(10, 7, 2, 8)
        Square.save_to_file([sq])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) == 39)
            
    def test_save_to_file_none_square(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

    def test_save_to_file_empty_list_square(self):
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual("[]", f.read())

class testIfBasedLoad(unittest.TestCase):
    @classmethod
    def cleanUp(self):
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_load_from_file_first_rect(self):
        rect1 = Rectangle(4, 5, 6, 7, 1)
        rect2 = Rectangle(8, 9, 10, 11, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rect[0]))

    def test_load_from_file_second_rect(self):
        rect1 = Rectangle(4, 5, 6, 7, 1)
        rect2 = Rectangle(8, 9, 10, 11, 2)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(str(rect2), str(list_rect[1]))

    def test_load_from_file_first_sq(self):
        sq1 = Square(4, 5, 6, 1)
        sq2 = Square(7, 8, 9, 2)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_sq[0]))

    def test_load_from_file_second_sq(self):
        sq1 = Square(4, 5, 6, 1)
        sq2 = Square(7, 8, 9, 2)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(sq2), str(list_sq[1]))

if __name__ == "__main__":
    unittest.main()
