#!/usr/bin/python3
def islower(c):
    value = ord(c) >= 97 and ord(c) < 123
    if value:
        return True
    return False
