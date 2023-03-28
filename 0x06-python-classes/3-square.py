#!/usr/bin/python3

"""Defines Square"""

class Square:
    """Reps area of square"""
    def __init__(self, size=0):
        """Initializes size
        Args:
        size(int): size of the square must be an integer"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__ = size

    def area(self):
        """Returns:
        the current square area"""
        return (self.__size * self.__size)
