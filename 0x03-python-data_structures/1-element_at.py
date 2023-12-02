#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def element_at(my_list, idx):
    count = num_len(my_list)
    if idx < 0 or idx > count:
        return None
    else:
        return my_list[idx]

    