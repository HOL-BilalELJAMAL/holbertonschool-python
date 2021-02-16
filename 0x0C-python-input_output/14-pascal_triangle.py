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
    if n <= 0:
        return [[]]
    triangle = []
    prev_row = []
    for i in range(0, n + 1):
        cur_row = [0 < j < i - 1 and i > 2 and prev_row[j - 1] +
                   prev_row[j] or 1 for j in range(0, i)]
        prev_row = cur_row
        triangle += [cur_row]
    return triangle[1:]
