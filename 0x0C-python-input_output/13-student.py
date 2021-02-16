#!/usr/bin/python3
"""
    13-student.py
    Module that defines a class called Student and returns Student's
    first_name, last_name and age
    Including method that retrieves a dictionary representation of a
    Student instance
    Including method that replaces all attributes of the Student instance
"""


class Student:
    """
    Represents a class called Student with a public instance
    attributes called first_name, last_name and age
    """

    def __init__(self, first_name, last_name, age):
        """Initialization of the public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Function that returns the dictionary representation of a
        Student instance

        Args:
            attrs (list): List of string attributes

        Note:
            If attrs is a list of strings, only elements in this list
            must be retrieved
            Otherwise, all attributes must be retrieved
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            my_dict = {}
            for key, val in self.__dict__.items():
                if key in attrs:
                    my_dict[key] = val
            return my_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """
        Function that replaces all attributes of the Student instance

        Args:
            json (dict): Dictionary of instance attributes
        """
        for key, val in json.items():
            self.__dict__[key] = val
