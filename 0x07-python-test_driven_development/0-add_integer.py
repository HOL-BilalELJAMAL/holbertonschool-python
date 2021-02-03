#!/usr/bin/python3
"""
    0-add_integer.py
    Module that defines a method for adding 2 integers
"""


def add_integer(a, b=98):
    """
    Function that takes two parameters as integers or floats and
    returns their addition as integer

    Args:
        a (int, float): First number
        b (int, float): Second number

    Note:
        If a is not an integer or a float, a TypeError exception is raised
        Else If b is not an integer or a float, a TypeError exception is raised
        Otherwise, cast a and b as integers and return their sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
