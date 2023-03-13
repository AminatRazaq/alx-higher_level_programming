#!/usr/bin/python3

def element_at(my_list, idx):
    """a function that retrieves an
    element from a list"""
    if idx < 0 or idx > len(my_list - 1):
        """I used len(my_list -1), -1 there
        is because index starts from 0 while
        length starts counting from 1"""
        return (None)
    return (my_list[idx])
