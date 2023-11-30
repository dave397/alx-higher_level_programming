#!/usr/bin/python3
import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div


def init(args):
    if args[2] == "+":
        return int(args[1]) + int(args[3])
    if args[2] == "-":
        return int(args[1]) - int(args[3])
    if args[2] == "*":
        return int(args[1]) * int(args[3])
    if args[2] == "/":
        return int(args[1]) / int(args[3])
    sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    print("{}".format(sys.argv[1]) + " " + "{}".format(sys.argv[2]) + " " +
          "{}".format(sys.argv[3]) + " = " + str(init(sys.argv)))
