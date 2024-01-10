#!/usr/bin/python3
def print_square(size):
    """prints a aquare

    Args:
        size (int): dimension for creting a square

    Raises:
        TypeError: if size is not integer
        ValueError: size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for a in range(size):
        [print("#", end="") for b in range(size)]
        print("")
    