#!/usr/bin/python3
'''5-save_to_json_file.py Module'''
import json


def save_to_json_file(my_obj, filename):
    '''Write object to text file by JSON representation'''
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
