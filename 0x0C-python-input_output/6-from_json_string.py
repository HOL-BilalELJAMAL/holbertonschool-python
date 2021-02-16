#!/usr/bin/python3
"""
    6-from_json_string.py
    Module that defines a function called to_json_string that returns
    an object (Python data structure) represented by a JSON string
"""


import json


def from_json_string(my_str):
    """
    Function that returns an object represented by a JSON string

    Args:
        my_str (str): JSON string
    """
    return json.loads(my_str)
