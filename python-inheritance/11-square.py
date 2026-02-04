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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Returns the following square description.
        """
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
