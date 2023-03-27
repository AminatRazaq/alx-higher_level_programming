#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """" a function that prints x elements of a list
    my_list: list consisting x elements
    x: elements in a my_list list
    Returns: the elements """

    counter = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            counter += 1
        except IndexError:
            break
    print("")
    return (counter)
