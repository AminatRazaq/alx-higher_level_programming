#!/usr/bin/python3

"""Defines a parent class-List and child class-MY List"""


class MyList(list):
    """displaying a parent and child class"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        return (sorted(self))
