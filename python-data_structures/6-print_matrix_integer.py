#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for index in range(len(line)):
            print("{}".format(line[index]), end="")
            if index != len(line) - 1:
                print("", end=" ")
        print()
