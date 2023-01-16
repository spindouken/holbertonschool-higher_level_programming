#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squared_matrix = []
    for row in matrix:
        row_copy = []
        for value in row:
            row_copy.append(value ** 2)
        squared_matrix.append(row_copy)
    return squared_matrix
