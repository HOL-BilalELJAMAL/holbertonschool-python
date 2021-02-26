#!/usr/bin/python3
"""
6-peak.py
Module that defines a method called find_peak that finds a peak
in a list of unsorted integers with lowest complexity
"""


def find_peak(list_of_integers):
    """
    Function that finds a peak in a list of unsorted integers
    with lowest complexity

    Args:
        list_of_integers (list): List of integers

    Note:
        if list_of_integers is not a list, return None
        else, return peak integer of the list using recursion
    """
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    else:
        peak = find_peak(list_of_integers[1:])
        return peak if peak > list_of_integers[0] \
            else list_of_integers[0]
