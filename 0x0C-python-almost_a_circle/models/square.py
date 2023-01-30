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
    
    def __str__(self):
        """str representation of Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
