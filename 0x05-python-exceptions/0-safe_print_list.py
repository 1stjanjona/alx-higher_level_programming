#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    p = 0
    for y in range(0, x):
        if x > p:
            try:
                print("{}".format(my_list[y]), end='')
            except Exception as exp:
                break
            else:
                p += 1
    print()
    return p
