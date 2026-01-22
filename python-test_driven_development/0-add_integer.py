#!/usr/bin/python3
"""
This module provides the function add_integer that adds two integers.
"""


def add_integer(a, b=98):
    """
    Function that adds two integers.
    Arguments of type floats are casted to integers before addition.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
