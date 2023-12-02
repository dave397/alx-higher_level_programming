#!/usr/bin/python3
def no_c(my_string):
    holder = ''
    for char in my_string:
        if char == 'C' or char == 'c':
            continue
        else:
            holder += char
    return holder
