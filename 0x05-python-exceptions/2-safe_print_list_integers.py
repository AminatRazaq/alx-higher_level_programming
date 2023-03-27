#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function that prints the first x elements
    of a list and only integers
    my_list:list with elements that can contain
    any type (integer, string, etc.)
    x: elements in a list"""
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            counter += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (counter)
