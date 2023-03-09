#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    """to add the numbers in each arguemebts together, not considering first arguement,
    so we regard the first arguement is absent and the second as the first arg"""
    num_in_arg = len(sys.argv) - 1
    sum = 0
    """set sum as 0"""
    for i in range(num_in_arg):
        sum += int(sys.argv[i + 1])
        print("{}".format(sum))
