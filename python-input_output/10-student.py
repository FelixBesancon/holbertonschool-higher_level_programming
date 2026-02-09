#!/usr/bin/python3
"""
This module provides the class Student, with:
    Public instance attributes:
        first_name
        last_name
        age
    Public method:
        to_json(self)
"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation
        of a Student instance.
        """
        if isinstance(attrs, list) and all(type(x) is str for x in attrs):
            student_dict = dict()
            for key in attrs:
                if key in self.__dict__:
                    student_dict[key] = self.__dict__[key]
            return student_dict

        return self.__dict__
