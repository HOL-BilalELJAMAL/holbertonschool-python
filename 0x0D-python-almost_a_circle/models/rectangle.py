#!/usr/bin/python3
"""
    rectangle.py
    Module that defines a class called Rectangle that inherits from
    Base and returns Rectangle width, height, horizontal displacement x,
    vertical displacement y and id (from Base)
    Including Getters and Setters
    Including Method to calculate the Rectangle's area
    Including Method to prints the rectangle using # character
    Including __str__ method to represent the Rectangle
    Including Method to update the attributes of the rectangle
    Including Method that returns the Rectangle's dictionary representation
"""

from models.base import Base


class Rectangle(Base):
    """
    Represents a class called Rectangle that inherits from Base
    with a private instance attributes called width, height, x, y
    and id (from Base)
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of the private instance attributes"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter property to get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle

        Args:
            value (int): New width of the Rectangle

        Note:
            If width is not an integer, a TypeError exception is raised
            Else If width is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter property to get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle

        Args:
            value (int): New height of the Rectangle

        Note:
            If height is not an integer, a TypeError exception is raised
            Else If height is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter property to get the horizontal displacement of the
        Rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the horizontal displacement of the Rectangle

        Args:
            value (int): New horizontal displacement of the Rectangle

        Note:
            If x is not an integer, a TypeError exception is raised
            Else If x is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not type(value) == int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter property to get the vertical displacement of the
        Rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the vertical displacement of the Rectangle

        Args:
            value (int): New vertical displacement of the Rectangle

        Note:
            If y is not an integer, a TypeError exception is raised
            Else If y is negative, a ValueError exception is raised
            Otherwise, Successful Set
        """
        if not type(value) == int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Function that prints the rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
        Function str that defines the string representation of the rectangle
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Function that assigns an argument to each attribute."""
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, e in enumerate(args):
                setattr(self, attrs[i], e)
            return
        for key, val in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, val)

    def to_dictionary(self):
        """Function that returns the rectangle's dictionary representation."""
        dict = {}
        for key, val in vars(self).items():
            dict[key.split("__")[-1]] = val
        return dict
