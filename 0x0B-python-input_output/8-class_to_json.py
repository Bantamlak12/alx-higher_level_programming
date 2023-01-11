#!/usr/bin/python3
"""Defines class to json"""


def class_to_json(obj):
    """Returns a dictionary with simple data structure..

    Args:
        obj: is instance of a class
    Returns:
        The dictionary description.
    """
    return obj.__dict__
