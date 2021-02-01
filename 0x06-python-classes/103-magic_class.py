#!/usr/bin/python3
"""
    103-magic_class.py
    Module that defines a MagicClass and return circle radius
    Including Methods to calculate the Circle's Area and Circumference
"""
import math


class MagicClass:
    """
    Represents a class called MagicClass with a private instance
    attribute called radius
    """

    def __init__(self, radius=0):
        """
        Initialization of the private instance attribute called radius
        
        Args:
            radius (int, float): radius of the Circle
        
        Note:
            If radius is not an integer and not float, a TypeError exception
            is raised
            Otherwise, Successful Initialization
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Function that returns the area of the Circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Function that returns the circumference of the Circle"""
        return 2 * math.pi * self.__radius
