#!/usr/bin/python3
''''2-is_same_class.py Module.'''


def is_same_class(obj, a_class):
    '''Return True if obj isinstance, else False.'''
    return type(obj) is a_class
