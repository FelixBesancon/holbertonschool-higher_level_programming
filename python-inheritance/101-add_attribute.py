#!/usr/bin/python3
"""Module that provides a function to add attributes to objects."""


def add_attribute(obj, attr, value):
    """Add a new attribute to an object if possible.

    Args:
        obj: The target object.
        attr (str): Name of the attribute to add.
        value: Value of the attribute.

    Raises:
        TypeError: If the object cannot receive new attributes.
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
