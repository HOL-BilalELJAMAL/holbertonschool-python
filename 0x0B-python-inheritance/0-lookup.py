#!/usr/bin/python3
"""
    0-lookup.py
    Module that defines a function that returns the list
    of available attributes and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object

    Args:
        obj: Object instance of certain class
    """
    return dir(obj)
