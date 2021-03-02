#!/usr/bin/python3
"""
0-validate_utf8.py
Module that defines a function called validUTF8 that determines if a
given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Function that determines if a given data set represents a valid
    UTF-8 encoding

    Args:
        data (list): List of integers
    """
    index = 0
    while index < len(data):
        number = data[index] & (2 ** 7)
        number >>= 7
        if number == 0:
            index += 1
            continue

        number_of_ones = 0
        while True:
            number = data[index] & (2 ** (7 - number_of_ones))
            number >>= (7 - number_of_ones)
            if number == 1:
                number_of_ones += 1
            else:
                break

            if number_of_ones > 4:
                return False

        if number_of_ones == 1:
            return False

        index += 1

        if index >= len(data) or index >= (index + number_of_ones - 1):
            return False

        for i in range(index, index + number_of_ones - 1):
            number = data[i]

            number >>= 7
            if number != 1:
                return False
            number >>= 7
            if number != 0:
                return False

            index += 1
    return True
