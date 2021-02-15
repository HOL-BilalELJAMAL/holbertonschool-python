#!/usr/bin/python3
"""
    101-add_attribute.py
    Module that defines a function called add_attribute that adds
    a new attribute to an object if its possible
"""


def add_attribute(obj, key, value):
    """
    Adds a new attribute to an object if possible

    Args:
        obj: Object instance of certain class
        key: Key of the attribute
        value: Value of the attribute

    Note:
        If the object can't have new attribute, a TypeError exception is raised
        Otherwise, set attribute
    """
    if (not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"))\
            or (hasattr(obj, "__slots__") and not hasattr(obj, key)):
        raise TypeError("can't add new attribute")
    setattr(obj, key, value)
