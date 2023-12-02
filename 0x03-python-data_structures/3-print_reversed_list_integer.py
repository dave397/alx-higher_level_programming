#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def print_reversed_list_integer(my_list=[]):
    count = num_len(my_list)

    while (count > 0):
        print("{:d}".format(my_list[count - 1]))
        count -= 1
