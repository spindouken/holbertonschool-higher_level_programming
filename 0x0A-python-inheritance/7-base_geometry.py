#!/usr/bin/python3
"""BaseGeometry module"""


class BaseGeometry:
    """Class of BaseGeometry"""

    def area(self):
        """raises an exception error with message"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value
        Args:
            name (str): string
            value (int): integer
        """

        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
