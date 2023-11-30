#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def init(args):
    a = int(args[1])
    b = int(args[3])
    
    if args[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))  
    elif args[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))  
    elif args[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))  
    elif args[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))  
    else:
        sys.stderr.write("Unknown operator. Available operators: +, -, * and /\n")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        sys.stderr.write("Usage: ./100-my_calculator.py <a> <operator> <b>\n")
        sys.exit(1)

    init(sys.argv)

