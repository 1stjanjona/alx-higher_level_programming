#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    ndx = 0
    lngth = 0
    while True:
        try:
            if my_list[lngth] is None:
                break
            lngth += 1
        except IndexError:
            break

    while ndx < min(x, lngth):
        print(my_list[ndx], end="")
        ndx += 1
    print()
    return ndx
