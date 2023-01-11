#!/usr/bin/python3
"""A function that returns the JSON representation of an object"""
import json


def to_json_string(my_obj):
    """
    Args:
        my_obj (str): an object(string) to be converted to JSON representation

    Returns:
        JSON representation
    """
    return json.dumps(my_obj)
