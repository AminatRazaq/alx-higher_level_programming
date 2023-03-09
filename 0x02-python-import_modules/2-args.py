#!/usr/bin/python3
if __name__ == "__main__":
    """sys. argv is a list that has all the command-line args passed"""
    """tto use sys.arg, you import modeule of "sys" using import sys"""
    import sys
    """num_arg = len(sys.argv)"""
    """the question doesn't recognise the normal first arg,so:"""
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0 arguments.")
    elif num_arg == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_arg))
        for i in range(num_arg):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
