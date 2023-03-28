#!/usr/bin/python3

"""defines a square with size validation"""


class Square:
    """Reps square with size"""
    def __init__(self, size=0):
        """Initializes size

    Args:
    size(int): the size must be an integer
    else
    raise Typeaerror with a message "size must be an integer"
    If size is less than 0, raise a ValueError
    exception with the message size must be >= 0"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size 
