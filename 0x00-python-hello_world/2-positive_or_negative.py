#!/usr/bin/python3
import random

number = random.randint(-10, 10)

if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("0 is zero")
else:
    print("{} is negative".format(number))
