#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """deletes keys with a specific value in a dictionary"""
    list_keys = list(a_dictionary.keys())

    for val_u in list_keys:
        if value == a_dictionary.get(val_u):
            del a_dictionary[val_u]
    return (a_dictionary)
