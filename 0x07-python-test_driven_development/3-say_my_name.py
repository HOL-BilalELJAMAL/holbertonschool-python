#!/usr/bin/python3
"""
    3-say_my_name.py
    Module that defines a method for printing the full name
    based on first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that takes a first_name and last_name as strings
    and prints a new string as full name with the following format:
    My name is <first name> <last name>

    Args:
        first_name (str): First name
        last_name (str): Last name

    Note:
        If first_name is not a string, a TypeError exception is raised
        If last_name is not a string, a TypeError exception is raised
        Otherwise, print a new string including the concatenation of
        first_name and last_name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
