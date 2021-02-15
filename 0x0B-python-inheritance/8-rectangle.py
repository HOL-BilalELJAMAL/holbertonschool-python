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
    Width and Height values will be validated using the integer_validator
    function implemented in the base class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
