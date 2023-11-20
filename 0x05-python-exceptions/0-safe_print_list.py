#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    printed_elements = 0
    for y in range(0, x):
        try:
            print("{}".format(my_list[y]), end='')
        except Exception as exp:
            break
        else:
            printed_elements += 1
    print()
    return printed_elements
