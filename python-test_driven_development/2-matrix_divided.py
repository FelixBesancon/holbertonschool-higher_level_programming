#!/usr/bin/python3
"""
This module provides the function matrix_divided
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not the same size
        TypeError: If div is not a number (integer or float)
        ZeroDivisionError: If div is equal to zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                    )
    row_size = len(matrix[0])
    for row in matrix:
        if row_size != len(row):
            raise TypeError(
                "Each row of the matrix must have the same size"
                )
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(round(value / div, 2))
        new_matrix.append(new_row)
    return new_matrix
