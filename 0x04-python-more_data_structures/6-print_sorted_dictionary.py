#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    list_keys = list(a_dictionary.keys())
    """after listing the keys, we now sort them alphabetically"""
    list_keys.sort()
    for i in list_keys:
        print("{}: {}".format(i, a_dictionary.get[i]))
