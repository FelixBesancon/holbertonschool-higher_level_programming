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
    skip_letter = False
    for letter in text:
        if skip_letter == False:
            print("{}".format(letter), end="")
        elif skip_letter == True and letter == " "
        if letter in (".", "?", ":"):
            print("\n")
