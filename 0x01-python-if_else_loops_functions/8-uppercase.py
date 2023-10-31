#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            up = chr(ord(c) - 32)
        else:
            up = c
        print("{}".format(up), end='')
    print()
