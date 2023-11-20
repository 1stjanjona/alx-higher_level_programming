#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed_elements = 0
    try:
        while y in range(x):
            print(my_list[y], end='')
            printed_elements += 1
    except IndexError:
        pass
    print()
    return printed_elements
