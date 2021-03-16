#!/usr/bin/python3
"""
    8-rectangle.py
    Module that defines a class called Rectangle that inherits from
    class BaseGeometry and returns its width and height
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
