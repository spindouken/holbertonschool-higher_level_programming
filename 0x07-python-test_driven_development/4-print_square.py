#!/usr/bin/python3
"""you want print square? look below vv ;] vv"""


def print_square(size):
    """
    prints a square of size `size` with the character "#"

    Args:
        size: size of the square
        type: int

    Raises:
        TypeError: if the input is not an integer
        ValueError: if the input is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for x in range(size):
        print("#" * size)
