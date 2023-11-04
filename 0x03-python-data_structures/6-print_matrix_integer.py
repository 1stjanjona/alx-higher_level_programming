#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for lists in matrix:
        if len(lists) == 0:
            print()
        for ndx in range(0, len(lists)):
            if ndx == len(lists) - 1:
                print("{:d}".format(lists[ndx]), end="\n")
            else:
                print("{:d}".format(lists[ndx]), end=" ")
