#!/usr/bin/python3
"""
    8-load_from_json_file.py
    Module that defines a function called load_from_json_file that that creates
    an Object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file

    Args:
        filename (file): File name

    Notes:
        Content of filename should be converted to string using JSON decoder
    """
    with open(filename) as f:
        return json.load(f)
