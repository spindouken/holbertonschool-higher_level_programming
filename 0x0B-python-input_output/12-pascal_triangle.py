#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers
    representing the Pascal’s triangle of n
    n: number of rows
    """

    if n <= 0:
        return ""

    pascals_triangle = [[1]]
    for current_row in range(1, n):
        row = [1]
        previous_row = pascals_triangle[current_row - 1]
        for element in range(1, current_row):
            row.append(previous_row[element] + previous_row[element - 1])
        row.append(1)
        pascals_triangle.append(row)
    return pascals_triangle
