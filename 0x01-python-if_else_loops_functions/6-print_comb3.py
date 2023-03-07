#!/usr/bin/python3
for num in range(0, 10):
    for dec in range(num + 1, 10):
        if num == 8 and dec == 9:
            print("{}{}".format(num,dec))
        else:
            print("{}{}".format(num,dec), end=", ")
