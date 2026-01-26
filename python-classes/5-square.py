#!/usr/bin/python3
"""
This module defines the class Square.
"""


class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initializes a Square instance with a given size.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square after validation.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Returns the area of the square.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square in stdout with the character '#'.
        """
        if self.size == 0:
            print()
        else:
            for row in range(self.size):
                for column in range(self.size):
                    print("{}".format("#"), end="")
                print()
