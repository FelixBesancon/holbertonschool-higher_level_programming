#!/usr/bin/python3
"""Module that inserts a line in a text file after a given string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a new line after each line containing a given string.

    The function reads the file content, then rewrites the file by adding
    new_string immediately after every line containing search_string.

    Args:
        filename (str): Name of the file to modify.
        search_string (str): String to search for in each line.
        new_string (str): String to insert after matching lines.
    """
    with open(filename, "r", encoding="utf-8") as f:
        new_content = ""
        for line in f:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, "w", encoding="utf-8") as f:
        f.write(new_content)
