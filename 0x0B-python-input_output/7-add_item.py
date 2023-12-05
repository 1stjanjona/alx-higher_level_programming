#!/usr/bin/python3
'''7-add_item.py Module'''
import json
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
jsonfile = "add_item.json"
data = []
if path.exists(jsonfile):
    data = load_from_json_file(jsonfile)
data.extend(sys.argv[1:])
save_to_json_file(data, jsonfile)
