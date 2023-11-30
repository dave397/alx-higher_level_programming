#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    print("{}".format(arg_len - 1) + " arguments.")
    if arg_len > 1:
        for i in range(1, arg_len):
            print("{}".format(i) + ": " + "{}".format(sys.argv[i]))
