#!/usr/bin/python3
"""class Rectangle is also based
    due to inheritating the basedness
"""
from models.base import Base


class Rectangle(Base):
    """
    create based class rectangle which is based off based Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize based rectangle values width, height, x, y, and id

        Based Args:
            width: width of rectangle
            height: height of rectangle
            x: x coordinate of rectangle
            y: y coordinate of rectangle
            id: id of rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width of based rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of based rectangle"""
        self.__width = value

    @property
    def height(self):
        """returns height of based rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of based rectangle"""
        self.__height = value

    @property
    def x(self):
        """returns x coordinate of based rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x coordinate of based rectangle"""
        self.__x = value

    @property
    def y(self):
        """returns x coordinate of based rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y coordinate of based rectangle"""
        self.__y = value
