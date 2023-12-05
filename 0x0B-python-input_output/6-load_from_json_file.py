#!/usr/bin/python3
'''6-load_from_json_file.py Module'''
import json


def load_from_json_file(filename):
    '''Create an Object'''
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
