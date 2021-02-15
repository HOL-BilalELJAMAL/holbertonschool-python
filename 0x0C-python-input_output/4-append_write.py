#!/usr/bin/python3
"""
    4-append_write.py
    Module that defines a function called append_write that appends a string
    at the end of a text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that appends a string to the end of a text file and returns
    the number of characters added

    Args:
        filename: File name
        text: Text to be appended to the file

    Notes:
        If file if does not exist, file should be created
        If file already exists, append text to the the end of the file
    """
    with open(filename, 'a') as f:
        return f.write(text)
