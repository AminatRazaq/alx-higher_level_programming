#!/usr/bin/python3

def max_integer(my_list=[]):
    """ finds the biggest integer of a list"""
    if len(my_list) == 0:
        return (None)
    """Initialize the maxi"""
    maxi = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > maxi:
            maxi = my_list[i]
        """then goes back to check the next element in the iteration"""
    return (maxi)
