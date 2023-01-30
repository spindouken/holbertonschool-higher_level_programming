#!/usr/bin/python3
"""class Square is also based
    due to inheritating the basedness
    from Rectangle which inherited it's basedness
    from based Base
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    create based class Square which is based off based Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize based Square values size, x, y, and id

        Based Args:
            size: size of square
            x: x coordinate of square
            y: y coordinate of square
            id: id of rectangle
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
            """returns size of based square"""
            return self.width

    @size.setter
    def size(self, size):
        """sets size of based square"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes
        **kwargs can be thought of as a double pointer
            to a dictionary: key/value
        """
        argList = ["id", "size", "x", "y"]

        if args and len(args) != 0:
            for i in range(len(args)):
                setattr(self, argList[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dictionary representation of based rectangle"""
        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }

    def __str__(self):
        """str representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
