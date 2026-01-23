#!/usr/bin/python3
"""
This module provides the function text_indentation
that prints a text with 2 new lines after each
of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Raises :
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    skip_space = False
    for letter in text:
        if skip_space == True and letter == " ":
            continue
        else:
            skip_space = False
        if letter in (".", "?", ":"):
            skip_space = True
            print("{}\n".format(letter))
            continue
        else:
            print("{}".format(letter), end="")
