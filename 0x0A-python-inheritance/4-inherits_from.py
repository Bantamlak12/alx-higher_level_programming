#!/usr/bin/python3
"""A module that checks for class inheritance."""


def inherits_from(obj, a_class):
    """Checks for class inheritance

    Args:
        obj (any): Object to be checked
        a_class (type): The class to match the type of obj to.
    
    Returns:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class ; otherwise False"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
