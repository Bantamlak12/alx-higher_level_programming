#!/usr/bin/python3
"""Defines a string from JSON to object"""
import json


def from_json_string(my_str):
    """returns object representated by a JSON string."""
    return json.loads(my_str)
