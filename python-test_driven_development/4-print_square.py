#!/usr/bin/python3
"""
This module provides the function print_square
that prints a square with the character #.
"""


def print_square(size):
    """
    Function that prints a square with the character #.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.
        TypeError: If size is a float and is less than 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        for column in range(size):
            print("{}".format("#"), end="")
        print()
