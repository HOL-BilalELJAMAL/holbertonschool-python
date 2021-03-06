#!/usr/bin/python3
"""
    1-rectangle.py
    Module that defines a Rectangle and returns Rectangle width and height
    Including Getters and Setters
"""


class Rectangle:
    """
    Represents a class called Rectangle with a private instance
    attributes called width and height
    """
    def __init__(self, width=0, height=0):
        """Initialization of the private instance attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter property to get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle

        Args:
            value (int): New width of the Rectangle

        Note:
            If width is not an integer, a TypeError exception is raised
            Else If width is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter property to get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle

        Args:
            value (int): New height of the Rectangle

        Note:
            If height is not an integer, a TypeError exception is raised
            Else If height is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
