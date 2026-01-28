#!/usr/bin/python3
"""
This module defines the class Rectangle with:
    Public class attribute:
        number_of_instances.
        print_symbol.
    Private instance attributes:
        width.
        height.
    Private instance property and setters:
        width.
        height.
    Static method:
        bigger_or_equal.
    Public instance methods:
        area.
        perimeter.
    Special instance method:
        __str__.
        __repr__.
        __del__.
"""


class Rectangle:
    """
    Represents a rectangle with:
        number_of_instances: The number of existing rectangles.
        print_symbol: The element to display when printing.
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle with:
            width: The horizontal size.
            height: The vertical size.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area, if both are equal,
        rect_1 is returned.

        Raises:
            TypeError: If either element is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area_1 = rect_1.area()
        area_2 = rect_2.area()
        if area_2 > area_1:
            return rect_2
        else:
            return rect_1

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
        using the '#' character, to be able to print by using
        print() and str().
        If width or height is equal to 0, an empty string is returned
        """
        rec_str = ""
        rec_line = ""
        if self.width != 0 and self.height != 0:
            rec_line += self.width * str(self.print_symbol)
            rec_str = (rec_line + '\n') * (self.height - 1) + rec_line
        return rec_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle,
        to be able to recreate a new instance by using eval().
        """
        rec_repr = str(self.__class__.__name__) + "("
        if self.width != 0 or self.height != 0:
            rec_repr += str(self.width) + ", " + str(self.height)
        rec_repr += ")"
        return rec_repr

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
