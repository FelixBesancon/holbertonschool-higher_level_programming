#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance with Fish,
Bird, and FlyingFish classes.
"""


class Fish:
    """Represents a fish."""

    def swim(self):
        """Print a message indicating the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the habitat where the fish lives."""
        print("The fish lives in water")

class Bird:
    """Represents a bird."""

    def fly(self):
        """Print a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the habitat where the bird lives."""
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """Represents a flying fish inheriting from Fish and Bird."""

    def swim(self):
        """Print swimming behavior of a flying fish."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print flying behavior of a flying fish."""
        print("The flying fish is soaring!")

    def habitat(self):
        """PPrint the habitat of a flying fish."""
        print("The flying fish lives both in water and the sky!")
