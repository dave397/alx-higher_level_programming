#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outer = len(matrix)
    inner = len(matrix[0])
    new_matrix = []
    for _ in range(outer):
        new_matrix.append([0] * inner)

    for x in range(outer):
        for y in range(inner):
            new_matrix[x][y] = matrix[x][y]**2

    return new_matrix
