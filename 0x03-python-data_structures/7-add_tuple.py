#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """adds 2 tuples"""
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    """if tuple_a is less than 2, so the no of elements is 0 or 1"""
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])