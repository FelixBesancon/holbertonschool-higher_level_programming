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
    pascal_list = []
    if n > 0:
        row = 1
        for row in range(n):
            pascal_list_int = []
            column = 1
            for column in range(row + 1):
                pascal_list_int.append(1)
                if 1 <= column < row:
                    pascal_list_int[column] = pascal_list[row - 1][column - 1] + pascal_list[row - 1][column]
            pascal_list.append(pascal_list_int)
    return pascal_list
