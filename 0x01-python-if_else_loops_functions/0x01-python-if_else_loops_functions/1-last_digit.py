#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = (abs(number) % 10) * -1
str = "Last digit of {} is {} and ".format(number, last_digit)
if last_digit > 5:
    str += "is greater than 5"
elif last_digit == 0:
    str += "is zero"
elif last_digit < 6 and last_digit != 0:
    str += "is less than 6 and not 0"
print(str)

