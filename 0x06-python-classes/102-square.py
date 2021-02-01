#!/usr/bin/python3
"""
    102-square.py
    Module that defines a Square and return square size
    Including Getters and Setters
    Including Method to calculate the Square's area
    Including all comparators functions based on Square's area
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

    def __eq__(self, other):
        """
        Function that return true when areas of the class instances
        are equal
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Function that return true when class instance 1 area
        is not equal class instance 2 area
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Function that return true when class instance 1 area
        is greater than class instance 2 area
        """
        return self.area() > other.area()

    def __lt__(self, other):
        """
        Function that return true when class instance 1 area
        is less than class instance 2 area
        """
        return self.area() < other.area()

    def __ge__(self, other):
        """
        Function that return true when class instance 1 area
        is greater than or equal class instance 2 area
        """
        return self.area() >= other.area()

    def __le__(self, other):
        """
        Function that return true when class instance 1 area
        is less than or equal class instance 2 area
        """
        return self.area() <= other.area()
