#!/usr/bin/python3

def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    """(<score>, <weight>)"""
    if not my_list:
        return (0)
    score_n_weight = 0
    weight_sum = 0
    for i in my_list:
        score_n_weight += i[0] * i[1]
        weight_sum += i[1]

    return (score_n_weight / weight_sum)
