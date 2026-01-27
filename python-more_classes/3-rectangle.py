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

    def area(self):
        """
        Returns the area of the rectangle, calculated with
        the multiplication of width and height.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle, calculated by
        adding every length, or 0 if either width or height is null.
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Returns a string representation of the rectangle,
        using the '#' character.
        If width or height is equal to 0, an empty string is returned
        """
        rec_str = ""
        rec_line = ""
        if self.width != 0 and self.height != 0:
            rec_line += self.width * '#'
            rec_str = (rec_line + '\n') * (self.height - 1) + rec_line
        return rec_str
