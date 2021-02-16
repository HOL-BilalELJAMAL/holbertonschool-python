#!/usr/bin/python3
"""
    14-pascal_triangle.py
    Module that defines a method called pascal_triangle that
    returns a list of lists of integers representing the Pascals
    triangle of height n
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the Pascals
    triangle of height n

    Args:
        n (int): Pascal's triangle height

    Note:
        if n<=0, return empty list of list
        Otherwise, return Pascal's triangle in list of list
    """
    triangle = []
    for i in range(n):
        row = [1]
        if i > 0:
            for j in range(i):
                row.append(sum(triangle[-1][j:j + 2]))
        triangle.append(row)
    return triangle
