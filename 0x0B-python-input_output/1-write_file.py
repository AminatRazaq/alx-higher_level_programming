#!/usr/bin/python3

"""Defines a file write function"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Args:
        filename(str): the name of the file
        text(str): text to wite the file 
    Returns :
        the number of characters written"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
