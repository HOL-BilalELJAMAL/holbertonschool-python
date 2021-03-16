#!/usr/bin/python3
"""
    10-square.py
    Module that defines a class called Square that inherits from
    class Rectangle and returns its size
    Including a method to calculate the Square's area
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a class called Rectangle with a private instance
    attribute called size
    """

    def __init__(self, size):
        """
        Initialization of the private instance attribute
        Size will be validated using the integer_validator
        implemented in the base class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__size ** 2
