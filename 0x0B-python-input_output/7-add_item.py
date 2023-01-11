#!/usr/bin/python3
"""Adds all arguments to a python list"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv
filename = "add_item.json"

try:
    py_list = load_from_json_file(filename)
except FileNotFoundError:
    py_list = []
py_list.extend(args[1:])
save_to_json_file(py_list, filename)
