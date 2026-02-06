#!/usr/bin/env python3
"""
Module designing two mixin classes, SwimMixin and FlyMixin,
with methods swim and fly, and class Dragon that inherits
from both these mixins.
"""


class SwimMixin:
    """Mixin that adds swimming capability."""

    def swim(self):
        """Print a message indicating the creature is swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying capability."""

    def fly(self):
        """Print a message indicating the creature is flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Represents a Dragon that swims and flies."""

    def roar(self):
        """Print a message indicating the dragon roars."""
        print("The dragon roars!")
