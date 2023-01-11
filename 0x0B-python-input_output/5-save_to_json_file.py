#!/usr/bin/python3
"""Save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation."""
    with open(filename, "w", encoding='utf-8') as a_file:
        txt = json.dumps(my_obj)
        return a_file.write(txt)
