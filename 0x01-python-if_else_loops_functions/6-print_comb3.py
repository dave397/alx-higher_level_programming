#!/usr/bin/python3
for i in range(0, 10):
    for e in range(0, 10):
        if i < e:
            if i == 8 and e == 9:
                print(f"{i}{e}")
            else:
                print(f"{i}{e}, ", end="")
