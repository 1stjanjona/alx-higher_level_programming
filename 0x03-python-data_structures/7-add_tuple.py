#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 0:
        tup_a_0 = tuple_a[0]
    else:
        tup_a_0 = 0
    if len(tuple_a) > 1:
        tup_a_1 = tuple_a[1]
    else:
        tup_a_1 = 0
    if len(tuple_b) > 0:
        tup_b_0 = tuple_b[0]
    else:
        tup_b_0 = 0
    if len(tuple_b) > 1:
        tup_b_1 = tuple_b[1]
    else:
        tup_b_1 = 0
    return (tup_a_0 + tup_b_0, tup_a_1 + tup_b_1)
