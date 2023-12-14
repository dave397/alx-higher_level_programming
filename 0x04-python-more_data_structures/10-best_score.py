#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    key = ''
    if not a_dictionary:
        return None

    for item in a_dictionary:

        if a_dictionary[item] > max:
            max = a_dictionary[item]
            key = item
    if max == 0:
        return None
    return key
