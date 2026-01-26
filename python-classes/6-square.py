#!/usr/bin/python3
"""
This module defines the class Square with:
    Private instance attributes:
        size.
        position.
    Private instance property and setters:
        size.
        position.
    Public class methods:
        area.
        my_print.
"""


class Square:
    """
    Represents a square with a size and a display position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square instance with:
            size.
            position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieves the current size of the square.
        """
        return self.__size

    @property
    def position(self):
        """
        Retrieves the current position of the square.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """
        Sets the size of the square after validation.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """
        Sets the position of the square after validation.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        pos_x, pos_y = value
        if (
            not isinstance(pos_x, int)
            or not isinstance(pos_y, int)
            or pos_x < 0
            or pos_y < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the area of the square,
        calculated with the square of 'size'.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square to standard output with the character '#',
        offset with 'position' by printing '\\n' and ' '.
        """
        pos_x, pos_y = self.position
        if self.size == 0:
            print()
        else:
            for row in range(self.size + pos_y):
                if row < pos_y:
                    print()
                else:
                    for column in range(self.size + pos_x):
                        if column < pos_x:
                            print("{}".format(" "), end="")
                        else:
                            print("{}".format("#"), end="")
                    print()
