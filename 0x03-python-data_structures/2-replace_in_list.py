#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """a function that replaces an element
    of a list at a specific position"""
    if idx < 0 or idx > (len(my_list) - 1):
        """I used len(my_list -1), -1 there
        is because index starts from 0 while
        length starts counting from 1"""
        return (my_list)
    mylist[idx] = element
