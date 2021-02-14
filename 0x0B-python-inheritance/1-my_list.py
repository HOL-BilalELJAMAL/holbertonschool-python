#!/usr/bin/python3
"""
    1-my_list.py
    Module that defines a class called MyList that inherits from list
    Includes a method that prints the list in ascending order
"""


class MyList(list):
    """Represents a class called MyList that inherits from list"""

    def print_sorted(self):
        """Method that prints the list in ascending order"""
        print(sorted(self))
