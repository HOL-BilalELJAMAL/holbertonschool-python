#!/usr/bin/python3
"""
    square.py
    Module that defines a class called Square that inherits from
    Rectangle and returns Square size, horizontal displacement x,
    vertical displacement y and id (from Rectangle)
    Including Getters and Setters
    Including __str__ method to represent the Square
    Including Method to update the attributes of the square
    Including Method that returns the Square's dictionary representation
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a class called Square that inherits from Rectangle
    with a private instance attributes called size, x, y
    and id (from Base)
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization of the private instance attributes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Function str that defines the string representation of the square
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter property to get the size of the Square"""
        return self.width

    @size.setter
    def size(self, size):
        """Set the size of the Square

        Args:
            size (int): New size of the Square
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Function that assigns an argument to each attribute."""
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def to_dictionary(self):
        """Return the dictionary representation of Square."""
        dict = {}
        for key, val in vars(self).items():
            if key.startswith("_"):
                if not key.endswith("width") and not key.endswith("height"):
                    idx = key.index("__")
                    dict[key[idx + 2:]] = val
                else:
                    dict["size"] = val
            else:
                dict[key] = val
        return dict
