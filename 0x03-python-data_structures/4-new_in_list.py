#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx not in range(0, len(my_list)):
        return my_list
    my_copied_list = my_list.copy()
    my_copied_list[idx] = element
    return my_copied_list
