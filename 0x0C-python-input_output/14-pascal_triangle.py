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
    res = []
    if n <= 0:
        return res
    for x in range(n):
        row = [1]
        if x > 0:
            for j in range(x):
                row.append(sum(res[-1][j:j + 2]))
        res.append(row)
    return res
