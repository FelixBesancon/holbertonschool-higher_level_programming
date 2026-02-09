#!/usr/bin/python3
"""
This module provide the function class_to_json,
that gives all attributes of an object.
"""


import json


def class_to_json(obj):
    """
    Returns the dictionary description with simple
    data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object.
    """
    return obj.__dict__
