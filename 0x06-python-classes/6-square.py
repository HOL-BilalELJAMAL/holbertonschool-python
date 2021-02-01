#!/usr/bin/python3
"""
    6-square.py
    Module that defines a Square and return square size and coordinates
    Including Getters and Setters
    Including Method to calculate the Square's area
    Including Method to print the Square based on coordinates
"""


class Square:
    """
    Represents a class called Square with:
        private instance attribute called size
        private instance attribute called position
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialization of the private instance attributes"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """Getter property to get the coordinates of the Square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the coordinates of the Square

        Args:
            value (tuple): New coordinates of the Square

        Note:
            If position contains more than 2 elements, a TypeError
            exception is raised
            Else If one of the position elements is negative, a TypeError
            exception is raised
            Else if one of the position elements is not integer, a TypeError
            exception is raised
            Otherwise, Successful Set
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(not isinstance(num, int) for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif any(num < 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Function that returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Function that prints the square based on coordinates

        Note:
            If size is zero, print empty line
            Otherwise:
                print matrix with # character of same Square's size
                with leading spaces based on coordinates
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print()
