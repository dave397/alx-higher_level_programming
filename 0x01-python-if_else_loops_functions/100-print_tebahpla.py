#!/usr/bin/python3
capitalize = False
for i in range(122, 96, -1):
    print("{}".format(chr(i).upper() if capitalize else chr(i)), end="")
    capitalize = not capitalize
