#!/usr/bin/python3

def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer"""
    uniq_int = set(my_list)
    sum = 0

    for i in uniq_int:
        sum += i
    return (sum)
