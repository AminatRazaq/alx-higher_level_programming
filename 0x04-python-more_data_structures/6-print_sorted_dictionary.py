#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
            print("{}: {}".format(i, a_dictionary.get(i)))
#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for k in sorted(my_dict.keys()):
        print("{}: {}".format(k, my_dict[k]))

