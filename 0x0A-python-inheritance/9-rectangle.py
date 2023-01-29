
#!/usr/bin/python3
"""Rectangle inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry"""
    def __init__(self, width, height):
        """__init__ - initialize a rectangle class
        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        return f"[Rectangle] {self.__width}/{self.__height}"
