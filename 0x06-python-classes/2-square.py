#!/usr/bin/python3

"""defines a square with size validation"""


class Square:
    """Reps square with size"""
    def __init__(self, size=0):
        """Initializes size

    Args:
    size(int): the sizeof the square and  must be an integer"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
