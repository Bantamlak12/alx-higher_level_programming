#!/usr/bin/python3
"""Adds a new attribute to an object if it's possible"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object.

    Args:
        obj (any): object to be created and set attribute for.
        name (str): name of the attribute of that object.
        value (any): gets the attribute passed.
    Raise:
        TypeError: if the object can't have a new attribute
    """
    if hasattr(obj, '__dict__'):
        return setattr(obj, name, value)
    raise TypeError("can't add new attribute")
