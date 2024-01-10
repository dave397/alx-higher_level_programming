#!/usr/bin/python3
"""Function Defines a Pascal's Triangle."""


def pascal_triangle(n):
    """Represent Triangle of size n(Pascal's).

    Returns a list of lists of integers.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
