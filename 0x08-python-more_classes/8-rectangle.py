#!/usr/bin/python3
"""
    8-rectangle.py
    Module that defines a Rectangle and returns Rectangle width and height
    Including Getters and Setters
    Including Method to calculate the Rectangle's area
    Including Method to calculate the Rectangle's perimeter
    Including __str__ method to represent the Rectangle using # character
    Including __repr__ method to represent the Rectangle using # character
    to be able to recreate a new instance by using eval()
    Including __del__ method that prints a message on object destruction
    Including class attribute to count the number of instances of objects
    Including class attribute to set the symbol used when printing
    the rectangle
    Including a static method to compare 2 rectangles by areas
"""


class Rectangle:
    """
    Represents a class called Rectangle with a private instance
    attributes called width and height
    """

    # A class variable, counting the number of instances
    number_of_instances = 0

    # A class variable, representing the symbol used when printing
    # the rectangle
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialization of the private instance attributes"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            raise ValueError("width must be >= 0")
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
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Function that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Function that returns the perimeter of the rectangle"""
        perm = 0
        if self.__width != 0 and self.__height != 0:
            perm = 2 * (self.__width + self.__height)
        return perm

    def __str__(self):
        """
        Function str that defines the string representation of the rectangle
        """
        rec_str = ""
        if self.__width == 0 or self.height == 0:
            return rec_str
        else:
            for i in range(self.__height):
                for j in range(self.width):
                    rec_str += str(self.print_symbol)
                rec_str += "\n"
            return rec_str[:-1]

    def __repr__(self):
        """
        Function repr that returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()
        """
        return "Rectangle(" + str(self.__width) + ", " \
               + str(self.__height) + ")"

    def __del__(self):
        """
        Function del that prints a message when an instance of class Rectangle
        is destroyed
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2
