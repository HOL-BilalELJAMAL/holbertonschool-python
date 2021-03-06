#!/usr/bin/python3
"""
    2-square.py
    Module that defines a Square and return square size
"""


class Square:
    """
    Represents a class called Square with a private instance
    attribute called size
    """
    def __init__(self, size=0):
        """
        Initialization of the private instance attribute called size

        Args:
            size (int): Size of the Square

        Note:
            If size is not an integer, a TypeError exception is raised
            Else If size is negative, a ValueError exception is raised
            Otherwise, Successful Initialization
        """
        if type(size) == int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")
