#!/usr/bin/env python3
"""
Module defining a CountedIterator class that counts
how many items have been iterated.
"""


class CountedIterator:
    """Iterator wrapper that counts retrieved items."""
    def __init__(self, iterable):
        """
        Initialize the counted iterator.

        Args:
            iterable: Any iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the number of items already iterated.

        Returns:
            int: Number of fetched items.
        """
        return self.counter

    def __next__(self):
        """
        Return the next item and increment the counter.

        Raises:
            StopIteration: When no items remain.

        Returns:
            The next item from the iterator.
        """
        value = next(self.iterator)
        self.counter += 1
        return value
