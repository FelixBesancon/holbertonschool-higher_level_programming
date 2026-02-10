#!/usr/bin/python3
"""
This module provides:
    serialize_and_save_to_file function:
        Serializes and saves data to the specified file
    load_and_deserialize:
        Loads and deserializes data from the specified file
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Function to serialize and save data to the specified file,
    with 2 parameters:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
        If the output file already exists it should be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Function to deserialize data from the specified file,
    with 1 parameter:
        filename: The filename of the input JSON file
    This function returns a Python Dictionary with
    the deseialized JSON data from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
