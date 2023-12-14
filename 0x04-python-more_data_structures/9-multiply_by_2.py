#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    holder = {}
    for item in a_dictionary:
        holder[item] = a_dictionary[item] * 2

    return holder
