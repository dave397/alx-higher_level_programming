#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    holder = sorted(a_dictionary.keys())
    for a in holder:
        print("{}: {}".format(a, a_dictionary[a]))
