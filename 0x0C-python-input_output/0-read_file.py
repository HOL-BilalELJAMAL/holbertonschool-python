#!/usr/bin/python3
"""
    0-read_file.py
    Module that defines a function called read_file that reads
    a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function that reads a text file and prints it to stdout

    Args:
        filename (file): File name
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
