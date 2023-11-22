#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        for y in range(x):
            print(my_list[y], end="")
            y += 1
        print()
        return y
    except IndexError:
        print()
        return y
