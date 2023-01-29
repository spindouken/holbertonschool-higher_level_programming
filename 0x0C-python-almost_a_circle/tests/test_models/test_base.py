#!/usr/bin/python3
"""
Based unittest for Base class
run with python3 -m unittest tests/base_test.py
or run with run all tests command:
    python3 -m unittest discover tests
OR just run it like a program! (thanks to bottom function)
"""
import unittest
from models import base
from models import rectangle 


class testIfBased(unittest.TestCase):
    def test_id_assignment_when_provided(self):
        """serves same purpose as if __nb_objects starts at 0
            and increments by 1"""
        base1 = Base(1)
        base2 = Base(2)
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_none(self):
        """testing if Base id assigned as None will still be incremented"""
        base1 = Base(None)
        base2 = Base(None)
        self.assertEqual(base1.id, 3)
        self.assertEqual(base2.id, 4)

    def test_auto_id_generation(self):
        """leave Base id assignment blank
        checking to see if nb_object incrementer is working properly
        use self.assertEqual to check if id is equal to incremented value
        """
        base1 = Base()
        base2 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

if __name__ == "__main__":
    unittest.main()
