#!/usr/bin/python3
'''8-class_to_json.py Module'''
import json


def class_to_json(obj):
    '''Return dictionary description for JSON serialization of an object'''
    return obj.__dict__
