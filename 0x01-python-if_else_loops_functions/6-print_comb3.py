#!/usr/bin/python3
for i in range(0, 10):
    for e in range(1, 10):
        if i < e:
            if i == 8 and e == 9:
                print("{}{}".format(i,e), end="")
            else:
                print("{}{} ".format(i,e), end="")
print()
