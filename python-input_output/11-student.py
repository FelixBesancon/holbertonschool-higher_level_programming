#!/usr/bin/python3
"""
This module provides the class Student, with:
    Public instance attributes:
        last_name
        first_name
        age
    Public method:
        to_json(self)
"""


class Student:
    """Represents a student."""
    def __init__(self, first_name, last_name, age):
        """
        Initializes a student with:
            last_name
            first_name
            age
        """
        self.last_name = last_name
        self.first_name = first_name
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        for key, value in json.items():
            if key in self.__dict__:
                setattr(self, key, value)
