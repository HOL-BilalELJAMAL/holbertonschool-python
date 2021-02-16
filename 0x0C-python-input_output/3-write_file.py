#!/usr/bin/python3
"""
    3-write_file.py
    Module that defines a function called write_file that writes a string
    to a text file (UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file and returns
    the number of characters written

    Args:
        filename (file): File name
        text (str): Text to be added to the file

    Notes:
        If file if does not exist, file should be created
        If file already exists, overwrite the content of the file
    """
    with open(filename, 'w') as f:
        return f.write(text)
