#!/usr/bin/python3
"""Create object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""

    with open(filename) as a_file:
       return json.load(a_file)
