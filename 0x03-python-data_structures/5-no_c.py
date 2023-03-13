#!/usr/bin/python3

def no_c(my_string):
    """removes all characters c and C from a string"""
    new_string = ''
    """Above: we created a new empty string"""
    for char in my_string:
        if char != C and char != c:
            new_string += char

    print(new_string)
