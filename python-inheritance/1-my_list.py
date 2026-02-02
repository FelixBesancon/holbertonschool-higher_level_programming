#!/usr/bin/python3
"""
This module defines the class MyList
with inheritance of list type.
"""


class MyList(list):
    """
    Represents a list.
    """

    def print_sorted(self):
        """
        Prints a list of int, but sorted
        in ascending order.
        """
        print(sorted(self))
