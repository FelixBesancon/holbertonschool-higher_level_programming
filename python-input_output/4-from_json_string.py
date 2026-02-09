#!/usr/bin/python3
"""
This module provide the function from_json_string,
that converts a JSON string into an object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure),
    represented by a JSON string.
    """
    return json.loads(my_str)
