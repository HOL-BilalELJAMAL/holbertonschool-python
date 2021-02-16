#!/usr/bin/python3
"""
    100-append_after.py
    Module that defines a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that inserts a line of text to a file, after each line
    containing a specific string

    Args:
        filename (file): File name
        search_string (str): Offset string
        new_string (str): String to add after occurrence of offset string
    """
    with open(filename) as f:
        lines = f.readlines()

    new_lines = ""
    for line in lines:
        new_lines += line
        if search_string in line:
            new_lines += new_string

    with open(filename, 'w') as f:
        f.write(new_lines)
