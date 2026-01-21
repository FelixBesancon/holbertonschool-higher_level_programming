#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return 0
    for row in matrix:
        for index, value in enumerate(row):
            print("{:d}".format(value), end="")
            if index != len(row) - 1:
                print(" ", end="")
        print()
