#!/usr/bin/python3

"""Defines a file write function"""


def append_write(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename(str): the name of the file
        text(str): text to wite the file 
    Returns :
        the number of characters written"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
