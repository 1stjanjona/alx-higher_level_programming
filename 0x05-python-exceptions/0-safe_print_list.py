#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    printed_elements = 0
    try:
        for y in range(0, x):
            print("{}".format(my_list[y]), end='')
            printed_elements += 1
    except IndexError:
        pass
    print()
    return printed_elements