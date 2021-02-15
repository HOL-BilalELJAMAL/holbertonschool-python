#!/usr/bin/python3
"""
    7-base_geometry.py
    Module that defines a BaseGeometry and return empty dictionary
    Including Method to calculate the area
    Including Method to validate an integer
"""


class BaseGeometry:
    """Represents a class called BaseGeometry"""

    def area(self):
        """Function that raises a specific exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates an integer

        Args:
            value (int): Value to validate

        Note:
            If value is not an integer, a TypeError exception is raised
            Else If value is negative, a ValueError exception is raised
            Otherwise, Do Nothing
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
