#!/usr/bin/python3
"""
This module defines the class Rectangle.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle
    """

    def __init__(self, width, height):
        """
        Initializes an instance of Rectangle, with:
            Private attributes:
                __width
                __height
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Returns the area calculated by multiplying
        width with height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the following rectangle description.
        """
        return "[{}] {}/{}".format(
            "Rectangle",
            self.__width,
            self.__height
        )
