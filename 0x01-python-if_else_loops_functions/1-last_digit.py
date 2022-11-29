#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    reminder = number % 10
else:
    reminder = number - (number//-10 * -10)
if reminder == 0:
    print(f'Last digit of {number} is {reminder} and is 0')
elif reminder < 6:
    print(f'Last digit of {number} is {reminder} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {reminder} and is greater than 5')
