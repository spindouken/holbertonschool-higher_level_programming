#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for z in x:
            print("{} ".format(z), end="")
        print()
