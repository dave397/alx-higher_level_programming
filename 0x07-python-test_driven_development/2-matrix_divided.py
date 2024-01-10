#!/usr/bin/python3
"""matrix division function"""


def matrix_divided(matrix, div):
    """Divides all element in a given matrix

    Args:
        matrix (list): a list of list with elements as int/float
        div (int/float): divisor

    Raises:
        ZeroDivisionError: div is zero
        TypeError: matrix contains non numbers
        TypeError: matrix has different sizes
        TypeError: div is not int or float

    Returns:
        _type_: _description_
    """
    matrix_len = len(matrix)
    i = 1
    size = len(matrix[0])
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if (not isinstance(matrix, list) or matrix == [] or
        not all(isinstance(row, list) for row in matrix) or
        not all((isinstance(ele, (int, float)))
            for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    while i < matrix_len:
        if size == len(matrix[i]):
            i = i + 1
            continue
        else:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    return ([list(map(lambda num: round(num / div, 2),row)) for row in matrix])
    