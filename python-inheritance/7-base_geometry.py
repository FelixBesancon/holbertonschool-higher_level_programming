#!/usr/bin/python3
"""
This module defines the class BaseGeometry.
"""


class BaseGeometry:
    """
    Represents an object of class BaseGeometry.
    """

    def area(self):
        """
        Public instance method area not implemented yet.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method integer_validator validate a value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
