#!/usr/bin/python3
"""
This module defines the class Rectangle with:
    Private instance attributes:
        width.
        height.
    Private instance property and setters:
        width.
        height.
"""


class Rectangle:
    """
    Represents a rectangle.
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with:
            width.
            height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the current width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """
        Retrieves the current height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle after validation.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle after validation.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
