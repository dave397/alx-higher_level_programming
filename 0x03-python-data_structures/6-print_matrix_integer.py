#!/usr/bin/python3
def num_len(my_list=[]):
    count = 0
    for num in my_list:
        count += 1
    return count


def print_matrix_integer(matrix=[[]]):
    outer = num_len(matrix)
    inner = num_len(matrix[0])
    for i in range(outer):
        for e in range(inner):
            if e == num_len(matrix[0]) - 1:
                print("{:d}".format(matrix[i][e]), end="")
            else:
                print("{:d}".format(matrix[i][e]), end=" ")
        print()
