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

    def area(self):
        """Returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """returns an “informal” and printable string representation"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        recta = []
        for i in range(self.__height):
            [recta.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                recta.append("\n")
            return ("".join(recta))
