#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        sum_a_b = sum(a * b for a, b in my_list)
        sum_b = sum(b for a, b in my_list)
        if sum_b == 0:
            return 0
        return sum_a_b / sum_b
