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
