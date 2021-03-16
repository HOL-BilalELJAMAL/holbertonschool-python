#!/usr/bin/python3
"""
    4-inherits_from.py
    Module that defines a function that checks if the object is an
    instance of a class that inherited (directly or indirectly) from
    the specified class
"""


def inherits_from(obj, a_class):
    """
    Function that checks if an object is a sub class of a specific class

    Args:
        obj: Object under study
        a_class: Class under study

    Note:
        Returns true if obj is a sub class of a_class
        Returns false otherwise
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
