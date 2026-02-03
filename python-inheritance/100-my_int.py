#!/usr/bin/python3
"""
This module defines the class MyInt.
"""


class MyInt(int):
    """
    Represents a rebel int.
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
