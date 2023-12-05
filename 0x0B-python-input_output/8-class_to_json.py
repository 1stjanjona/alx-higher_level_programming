#!/usr/bin/python3
'''8-class_to_json.py Module'''
import json


def class_to_json(obj):
    '''Return dictionary description for JSON serialization of an object'''
    json_dict = {}
    if hasattr(obj, '__dict__'):
        for key, value in obj.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                json_dict[key] = value
    elif hasattr(obj, "__slots__"):
        for key in obj.__slots__:
            if hasattr(obj, key):
                value = getattr(obj, key)
                if isinstance(value, (list, dict, str, int, bool)):
                    json_dict[key] = value
    return json_dict
