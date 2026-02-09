#!/usr/bin/python3
"""
This module provides the function read_file,
that read and print a UTF-8 file.
"""


def read_file(filename=""):
    """
    Reads the content of a text file (UTF8),
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
