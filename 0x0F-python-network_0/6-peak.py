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
    """
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        return list_of_integers[0]
    n = len(list_of_integers) - 1
    idx = 0
    while n > idx:
        mid = (n + idx) // 2
        if list_of_integers[mid] <= list_of_integers[mid + 1]:
            idx = mid + 1
        elif list_of_integers[mid] <= list_of_integers[mid - 1]:
            n = mid - 1
        elif list_of_integers[mid] >= list_of_integers[mid + 1]\
                and list_of_integers[mid] >= list_of_integers[mid - 1]:
            return list_of_integers[mid]
    return list_of_integers[idx]
