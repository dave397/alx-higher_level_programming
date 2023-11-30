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
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    init(sys.argv)

