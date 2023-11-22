#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for y in range(x):
            print(my_list[y], end="")
        print()
        return y + 1
    except IndexError:
        print()
        return y
