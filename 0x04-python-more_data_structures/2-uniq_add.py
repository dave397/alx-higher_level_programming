#!/usr/bin/python3
def uniq_add(my_list=[]):
    holder = []
    sum = 0
    for num in my_list:
        if num not in holder:
            sum += num
            holder.append(num)

    return sum
