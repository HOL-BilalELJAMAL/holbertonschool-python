#!/usr/bin/python3
"""
    5-to_json_string.py
    Module that defines a function called to_json_string that returns
    the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object

    Args:
        my_obj (object): Object
    """
    return json.dumps(my_obj)
