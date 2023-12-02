#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def divisible_by_2(my_list=[]):
    hold = num_len(my_list)
    b = my_list[:hold]
    count = 0
    for num in my_list:
        if num % 2 == 0:
            b[count] = True
        else:
            b[count] = False
        count += 1
    return b
