#!/usr/bin/python3
"""
    11-square.py
    Module that defines a class called Square that inherits from
    class Rectangle and returns its size
    Including a method to calculate the Square's area
    Including __str__ method to represent the Square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a class called Square with a private instance
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
        """Function that returns the area of the Square"""
        return self.__size ** 2

    def __str__(self):
        """
        Function str that defines the string representation of the Square
        """
        return "[Square] {}/{}".format(str(self.__size),
                                       str(self.__size))
