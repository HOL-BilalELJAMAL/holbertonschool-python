#!/usr/bin/python3
"""
    2-read_lines.py
    Module that defines a function called read_lines that
    reads n lines of a text file (UTF8) and prints it to stdout
"""


def read_lines(filename="", nb_lines=0):
    """
    Function that prints n lines of a text file to stdout

    Args:
        filename (file): File name
        nb_lines (int): Number of lines

    Notes:
        if nb_lines <= 0 or nb_lines > file number of lines
            Prints entire file
        Otherwise
            Prints nb_lines lines of the file
    """
    cnt = 0
    with open(filename) as f:
        for line in f:
            print(line, end="")
            cnt += 1
            if cnt == nb_lines and nb_lines > 0:
                break
