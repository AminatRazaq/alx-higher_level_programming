#!/usr/bin/python3

def best_score(a_dictionary):
    """returns a key with the biggest integer value"""
    if not a_dictionary:
        return (None)
    bigges_key = max(a_dictionary, key = lambda x: a_dictionary[x])
    return (biggest_key)
