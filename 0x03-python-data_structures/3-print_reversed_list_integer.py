#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """a function that prints all integers
    of a list, in reverse order"""
    my_list = my_list.reverse()

    for i in range(len(my_list)-1):
        print("{:d}".format(my_list[i]))
