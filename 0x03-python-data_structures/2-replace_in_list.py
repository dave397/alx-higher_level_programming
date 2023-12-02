#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def replace_in_list(my_list, idx, element):
    count = num_len(my_list)

    if idx < 0 or idx > count - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
