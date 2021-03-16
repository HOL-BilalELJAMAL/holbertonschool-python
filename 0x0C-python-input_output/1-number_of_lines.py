#!/usr/bin/python3
"""
    1-number_of_lines.py
    Module that defines a function called number_of_lines that
    returns the number of lines of a text file
"""


def number_of_lines(filename=""):
    """
    Function that returns the number of lines of a text file

    Args:
        filename (file): File name
    """
    nb_lines = 0
    with open(filename) as f:
        for line in f:
            nb_lines += 1
    return nb_lines
