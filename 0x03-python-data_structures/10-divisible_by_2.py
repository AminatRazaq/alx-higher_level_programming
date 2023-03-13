#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    """we create an empty list for the new list"""
    mul_of_2 = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            mul_of_2.append(True)
        else:
        mul_of_2.append(False)
    return (mul_of_2)
