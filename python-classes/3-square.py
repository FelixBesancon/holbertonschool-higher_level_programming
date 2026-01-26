#!/usr/bin/python3
"""
This module defines the class Square with:
    Private instance attribute size.
    Public class method area.
"""


class Square:
    """
    Represents a square with a size.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size
        after validation.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Returns the area of the square,
        calculated with the square of 'size'.
        """
        return self.__size ** 2
