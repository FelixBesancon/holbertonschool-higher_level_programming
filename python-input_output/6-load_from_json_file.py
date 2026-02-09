#!/usr/bin/python3
"""
This module provide the function load_from_json_file,
that creates an object from a JSON text file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an Object from to a text file,
    using a JSON representation.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
