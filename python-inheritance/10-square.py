#!/usr/bin/python3
"""
This module defines the class Square.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes an instance of Square, with:
            size.
        """
        self.__size = size
        super().__init__(size, size)
