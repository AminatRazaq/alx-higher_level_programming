#!/usr/bin/python3


def magic_calculation(a, b):
    result_mag = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result_mag += a ** b / i
        """EXCEPTION can be used as a wildcard that catches (almost)
        everything it is good practice to be as specific as possible
        with the types of exceptions that we intend to handle, and
        to allow any unexpected exceptions to propagate on"""
        except Exception:
            result_mag = b + a
            break
    return (result_mag)
