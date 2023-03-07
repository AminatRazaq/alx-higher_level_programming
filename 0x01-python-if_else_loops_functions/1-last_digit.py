#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_dig = number % 10#to find the last digit
if last_dig > 5:
    print("Last digit of {0} is {1}and is greater than 5".format(number, last_dig))
elif last_dig == 0:
    print("Last digit of {0} is {1} and is 0".format(number, last_dig))
else last_dig < 6 and last_dig != 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(number, last_dig))
