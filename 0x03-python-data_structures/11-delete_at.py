#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def delete_at(my_list=[], idx=0):
    count = num_len(my_list)
    if idx < 0 or idx > count - 1:
        return my_list
    del my_list[idx]

    return my_list
