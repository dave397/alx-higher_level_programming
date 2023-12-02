#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def max_integer(my_list=[]):
    max = my_list[0]
    count = num_len(my_list)
    for i in range(count):
        if my_list[i] > max:
            max = my_list[i]
    return max
