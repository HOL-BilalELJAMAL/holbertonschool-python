#!/usr/bin/python3
"""
0-minoperations.py
Module that defines a function called minOperations that calculates the fewest
number of operations needed to result in exactly n H
"""


def minOperations(n):
    """
    Function that calculates the fewest number of operations needed
    to result in exactly n H

    Args:
        n (int): length of H characters string

    Note:
        Allowed operations: Copy All and Paste
        if n<=1, return 0
        Otherwise, return minimum number of operations
    """
    offset = 2
    nb_operations = 0
    while n > 1:
        if n % offset == 0:
            n /= offset
            nb_operations += offset
        else:
            offset += 1
    return nb_operations
