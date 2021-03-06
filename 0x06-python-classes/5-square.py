#!/usr/bin/python3
"""
    5-square.py
    Module that defines a Square and return square size
    Including Getters and Setters
    Including Method to calculate the Square's area
    Including Method to print the Square
"""


class Square:
    """
    Represents a class called Square with a private instance
    attribute called size
    """
    def __init__(self, size=0):
        """Initialization of the private instance attribute called size"""
        self.size = size

    @property
    def size(self):
        """Getter property to get the size of the Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square

        Args:
            value (int): New size of the Square

        Note:
            If size is not an integer, a TypeError exception is raised
            Else If size is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if type(value) == int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Function that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Function that prints the square

        Note:
            If size is zero, print empty line
            Otherwise, print matrix with # character of same Square's size
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
