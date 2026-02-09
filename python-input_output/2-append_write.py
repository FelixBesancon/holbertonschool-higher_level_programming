#!/usr/bin/python3
"""
This module provides the function append_write,
that appends a string to a UTF-8 text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8),
    and returns the number of characters written.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
