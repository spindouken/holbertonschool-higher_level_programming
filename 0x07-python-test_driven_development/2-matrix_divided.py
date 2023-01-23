#!/usr/bin/python3
"""Divide all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix that has been divided

    Args:
        :matrix: a list of lists of ints or floats
        :div: number (int or float) to divide each element of matrix by

    Raises:
        :raise TypeError: if matrix is not a list of lists of ints or floats
        :raise TypeError: if rows have have a different size than first row
        :raise TypeError: if div is not a number (int or float)
        :raise ZeroDivisionError: if div is equal to 0
    """

    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in range(len(matrix)):
        if len(matrix[0]) != len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")
        for value in range(len(matrix[row])):
            if type(matrix[row][value]) != int and\
                    type(matrix[row][value]) != float:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    return [[round(value / div, 2) for value in row] for row in matrix]
