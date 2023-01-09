#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0
    flag = 1

lastDigit = abs(number) % 10

if flag = 1
    lastDigit = lastDigit * -1


print("Last digit of {} is {}".format(number, lastDigit), end="")
if lastDigit > 5:
    print(" and is greater than 5".format(number, lastDigit))
elif lastDigit == 0:
    print(" and is 0".format(number, lastDigit))
else:
    print(" and is less than 6 and not 0".format(number, lastDigit))
