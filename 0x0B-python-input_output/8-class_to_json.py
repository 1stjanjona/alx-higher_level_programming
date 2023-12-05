#!/usr/bin/python3
'''8-class_to_json.py Module'''
import json


def class_to_json(obj):
    '''Return dictionary description for JSON serialization of an object'''
    if hasattr(obj, '__dict__'):
        return obj.__dict__.copy()
    elif hasattr(obj, "__slots__"):
        for key in obj.__slots__:
            return {key: getatte(obj, key)}
    else:
        return {}
