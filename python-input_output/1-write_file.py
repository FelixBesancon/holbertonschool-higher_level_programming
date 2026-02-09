#!/usr/bin/python3
"""
This module provides the function write_file,
that writes a string to a UTF-8 text file.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8),
    and returns the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
