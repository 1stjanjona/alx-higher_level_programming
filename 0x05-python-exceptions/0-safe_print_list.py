#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    p = 0
    try:
        for y in range(0, x):
            if x > p:
                print("{}".format(my_list[y]), end='')
                p += 1
            else:
                break
    except IndexError:
        pass
    print()
    return p
