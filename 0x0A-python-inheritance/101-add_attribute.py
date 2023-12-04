#!/usr/bin/python3
'''101-add_attribute.py Module'''


def add_attribute(obj, a, value):
    '''Add new attribute if possible'''
    if not hasattr(obj, "__dict__"):
        raise TypeError('can\'t add new attribute')
    setattr(obj, a, value)
