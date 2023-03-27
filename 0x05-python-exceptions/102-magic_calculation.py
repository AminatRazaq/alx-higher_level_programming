#!/usr/bin/python3


def magic_calculation(a, b):
    result_mag = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result_mag += a ** b / i
        except Exception:
            result_mag = b + a
            break
    return (result_mag)
