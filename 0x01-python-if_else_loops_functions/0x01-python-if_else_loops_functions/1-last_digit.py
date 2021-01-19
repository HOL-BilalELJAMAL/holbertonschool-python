#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if number < 0:
    last_digit = (abs(number) % 10) * -1
message = "Last digit of " + str(number) + " is " + str(last_digit)
if last_digit > 5:
    print(message, "and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(message, "and is less than 6 and not 0")
else:
    print(message, "and is 0")
