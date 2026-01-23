#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not isintance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    row_size = len(matrix[1])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
