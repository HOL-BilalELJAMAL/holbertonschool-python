#!/usr/bin/python3
"""
    10-class_to_json.py
    Module that defines a method called class_to_json that
    returns the dictionary description with simple data structure
    for JSON serialization of an object
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data structure
    for JSON serialization of an object

    Args:
        obj (object): Object
    """
    return obj.__dict__
