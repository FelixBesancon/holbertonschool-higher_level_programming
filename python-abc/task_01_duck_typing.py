#!/usr/bin/python3
"""
This module defines:

The abstract class Shape, with abstract methods:
    area.
    perimeter.

The class Circle, subclass of Shape, with instance attribute:
    radius.

The class Rectangle, subclass of Shape, with instance attribute:
    width.
    height.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """
    Represents an abstract shape.
    """

    @abstractmethod
    def area(self):
        """Returns the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Returns the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    Represents a circle.
    """

    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        """Returns the area of a circle."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the perimeter of a circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle.
    """

    def __init__(self, width, height):
        self.width = abs(width)
        self.height = abs(height)

    def area(self):
        """Returns the area of a rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of a rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Prints the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
