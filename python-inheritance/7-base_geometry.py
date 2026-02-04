#!/usr/bin/python3
"""
This module defines the class BaseGeometry.

It includes an unimplemented area method and a validator for integer values.
"""


class BaseGeometry:
    """
    Represents an object of class BaseGeometry.

    This class defines common behavior for geometry-related classes,
    such as area computation (to be implemented by subclasses) and
    validation of integer parameters.
    """

    def area(self):
        """
        Public instance method area not implemented yet.

        Raises:
            Exception: Always, because this method must be implemented
            by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method integer_validator validate a value.

        Args:
            name (str): The name of the parameter to validate.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
