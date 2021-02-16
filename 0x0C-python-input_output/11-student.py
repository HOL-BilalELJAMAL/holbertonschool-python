#!/usr/bin/python3
"""
    11-student.py
    Module that defines a class called Student and returns Student's
    first_name, last_name and age
    Including method that retrieves a dictionary representation of a
    Student instance
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

    def to_json(self):
        """
        Function that returns the dictionary representation of a
        Student instance
        """
        return self.__dict__
