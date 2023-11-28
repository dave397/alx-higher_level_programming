#!/usr/bin/python3
capitalize = False
for i in range(122, 96, -1):
    if not capitalize:
        print(chr(i), end="")
        capitalize = True
    else:
        print(chr(i).upper(), end="")
        capitalize = False
