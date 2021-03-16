#!/usr/bin/python3
"""
    100-my_int.py
    Module that defines a class called MyInt that inherits from int
    such that the operators equals and not equals are inverted
"""


class MyInt(int):
    """
    Represents a class called MyInt that inherits from int
    """
    def __eq__(self, other):
        """Convert equal operator to not equal"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Convert not equal operator to equal"""
        return super().__eq__(other)
