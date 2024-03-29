#!/usr/bin/python3

def safe_print_division(a, b):
    """function that divides 2 integers and
    prints the result
    a and b: are the two integers in the division"""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
