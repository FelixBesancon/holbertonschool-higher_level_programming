#!/usr/bin/python3
"""
This module defines the class VerboseList,
extension of the type list.
"""


class VerboseList(list):
    """Represents a verbose list"""

    def append(self, item):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended the list with [{}] items.".format(len(item)))

    def remove(self, item):
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, item=None):
        if item is None:
            item = -1
        try:
            value = self[item]
        except IndexError:
            raise
        print("Popped [{}] from the list.".format(value))
        return super().pop(item)
