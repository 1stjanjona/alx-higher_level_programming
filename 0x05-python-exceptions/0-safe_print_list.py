#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        y = 0
        for y in range(min(x, len(my_list))):
            print(my_list[y], end="")
        print()
        return min(x, len(my_list))
    except IndexError:
        print()
        return y
