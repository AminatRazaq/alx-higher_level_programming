#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string"""


    """ join() returns a new string which is the concatenation
    of the other strings in the iterable specified"""
    copy = [x for x in my_string if x != 'C' and x!= 'c']
    """"Below: the "" in return is to show the new empty string"""
    return ("".join(copy))
