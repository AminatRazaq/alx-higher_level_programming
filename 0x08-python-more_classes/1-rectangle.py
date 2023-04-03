#!/usr/bin/python3

"""Defines Rectangle"""


class Rectangle:
    """Gives a Rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes width and heigth of a rectangle
        Args:
        width: width of a rectangle
        height: height of a rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """retriev width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height"""
        return(self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
