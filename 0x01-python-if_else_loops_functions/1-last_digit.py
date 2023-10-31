#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 10:
    modulu = number % 10
else:
    modulu = number % -10
print(f"Last digit of {number:d} is {modulu:d} and is ", end="")
if modulu > 5:
    print("greater than 5")
elif modulu == 0:
    print("0")
else:
    print("less than 6 and not 0")
