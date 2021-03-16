#!/usr/bin/python3
"""
    101-locked_class.py
    Module that defines a LockedClass
"""


class LockedClass:
    """Represents a locked class called LockedClass
    where only first_name class attribute can be set"""
    __slots__ = ['first_name']
