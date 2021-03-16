#!/usr/bin/python3
"""
    4-print_square.py
    Module that defines a method for printing a matrix square
    using # character based on size parameter
"""


def print_square(size):
    """
    Function that takes a size as integer and prints the matrix
    square using # character

    Args:
        size (int): Size of the square

    Note:
        If size is not an integer, a TypeError exception is raised
        If size is less than zero, a ValueError exception is raised
        If size is a float and less than zero, a TypeError exception
        is raised
        Otherwise, print the square using # character
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
