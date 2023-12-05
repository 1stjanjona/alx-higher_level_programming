#!/usr/bin/python3
'''8-class_to_json.py Module'''
import json


def class_to_json(obj):
    '''Return dictionary description for JSON serialization of an object'''
    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                return {key: value}
    elif hasattr(obj, "__slots__"):
        for key in obj.__slots__:
            if isinstance(getattr(obj, key), (list, dict, str, int, bool)):
                return {key: getattr(obj, key)}
    else:
        return {}
