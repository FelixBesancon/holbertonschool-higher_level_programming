#!/usr/bin/python3
"""
This module defines the inherits_from function.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class
    that inherited (directly or indirectly) from
    the specified class ; otherwise False.
    """
    obj_type = type(obj)
    return issubclass(obj_type, a_class) and obj_type != a_class
