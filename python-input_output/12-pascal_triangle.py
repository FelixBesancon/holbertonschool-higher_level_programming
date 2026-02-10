#!/usr/bin/python3
"""
This module provides the function pascal_triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n, Returns an empty list
    if n <= 0.
    """
    triangle = []
    if n > 0:
        for row in range(n):
            line = [1] * (row + 1)
            for column in range(row):
                if 1 <= column:
                    line[column] = (
                        triangle[row - 1][column - 1]
                        + triangle[row - 1][column]
                    )
            triangle.append(line)

    return triangle
