#!/usr/bin/python3

"""Defines a Class to JSON function"""


def class_to_json(obj):
    """a function that returns the dictionary description with simple data
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object structure"""
    return obj.__dict__
