#!/usr/bin/python3
"""
    7-save_to_json_file.py
    Module that defines a function called save_to_json_file that writes an
    Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an Object to a text file, using
    a JSON representation

    Args:
        my_obj (object): Object
        filename (file): File name

    Notes:
        Object should be converted to JSON String
        If file does not exist, file should be created including JSON String
        If file already exists, overwrite the file with JSON String
    """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
