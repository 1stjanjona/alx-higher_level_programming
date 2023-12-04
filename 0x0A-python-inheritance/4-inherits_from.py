#!/usr/bin/python3
'''4-inherits_from.py Module.'''


def inherits_from(obj, a_class):
    '''Return True for directly/indirectly inheritance, else False'''
    return isinstance(obj, a_class) and type(obj) is not a_class
