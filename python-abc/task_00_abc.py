#!/usr/bin/python3
"""
This module defines the class Animal,
and subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Represents an abstract animal.
    """
    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """
    Represents a dog, subclass of Animal.
    """
    def sound(self):
        """Return the sound made by the dog."""
        return "Bark"


class Cat(Animal):
    """
    Represents a cat, subclass of Animal.
    """
    def sound(self):
        """Return the sound made by the cat."""
        return "Meow"
