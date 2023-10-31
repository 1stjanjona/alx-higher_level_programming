#!/usr/bin/python3
for letter in range(25, -1, -1):
    alpha = letter + ord('A')
    if letter % 2 == 1:
        alpha += 32
    print("{:c}".format(alpha), end='')
