#!/usr/bin/python3
"""
    2-is_same_class.py
    Module that defines a function that checks if an object
    is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Function that checks if an object is an instance of a specific class

    Args:
        obj: Object under study
        a_class: Class under study

    Note:
        Returns true if obj is instance of a_class
        Returns false otherwise
    """
    return type(obj) == a_class
