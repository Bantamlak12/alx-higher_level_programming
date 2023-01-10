#!/usr/bin/python3
"""A module that tests for same class or inherited from"""


def is_kind_of_class(obj, a_class):
    """Checks an instance's type

    Args:
        obj (any): object to be checked
        a_class (type): The class to match the type of obj to.

    Returns:
        True if the object is an instance of a_class that inherited from,
        the specified class ; otherwise false.
    """
    return isinstance(obj, a_class)
