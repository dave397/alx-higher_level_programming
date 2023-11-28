#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
positive = True

if (number < 0):
    positive = False

last_digit = int(str(number)[-1:])

if (not positive):
    last_digit = int("-" + str(last_digit))

message = f"Last digit of {number} is {last_digit} and"
if last_digit > 5:
    print(f"{message} is greater than 5")
elif last_digit == 0:
    print(f"{message} is 0")
else:
    print(f"{message} is less than 6 and is not 0")
