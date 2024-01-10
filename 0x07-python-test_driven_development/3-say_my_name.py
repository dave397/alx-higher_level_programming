#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """function prints name

    Args:
        first_name (str): first name of entity
        last_name (str, optional): last name of entity. Defaults to "".

    Raises:
        TypeError: if either first_name or last_name is not string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
