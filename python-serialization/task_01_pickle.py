#!/usr/bin/python3
"""
This module provides the class CustomObject, with:
    Public instance attributes:
        name (a string)
        age (an integer)
        is_student (a boolean)
    Public class mathod:
        display(self)
        serialize(self, filename)
    Class method:
        deserialize(cls, filename)
"""


import pickle


class CustomObject:
    """Represents a custom object"""
    def __init__(self, name="", age=0, is_student=False):
        """Initializes an instance of ClassObjects, with:
            name
            age
            is_student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints out the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current instance of the object
        and save it to the provided filename.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Loads and returns an instance of the CustomObject
        from the provided filename.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None

            return obj

        except (
            FileNotFoundError, OSError, pickle.UnpicklingError,
            EOFError, AttributeError, ImportError, ModuleNotFoundError
        ):
            return None
