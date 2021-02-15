#!/usr/bin/python3
"""
    9-rectangle.py
    Module that defines a class called Rectangle that inherits from
    class BaseGeometry and returns its width and height
    Including a method to calculate the Rectangle's area
    Including __str__ method to represent the Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a class called Rectangle with a private instance
    attributes called width and height
    """

    def __init__(self, width, height):
        """
        Initialization of the private instance attributes
        Width and Height  will be validated using the integer_validator
        implemented in the base class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """
        Function str that defines the string representation of the rectangle
        """
        return "[Rectangle] {}/{}".format(str(self.__width),
                                          str(self.__height))
