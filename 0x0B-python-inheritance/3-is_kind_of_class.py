#!/usr/bin/python3
"""
    3-is_kind_of_class.py
    Module that defines a function that checks if an object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function that checks if an object is an instance of a specific class

    Args:
        obj: Object under study
        a_class: Class under study

    Note:
        Returns true if obj is instance of a_class
        Returns false otherwise
    """
    return isinstance(obj, a_class)
