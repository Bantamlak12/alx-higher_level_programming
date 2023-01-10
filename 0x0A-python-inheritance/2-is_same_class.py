#!/usr/bin/python3
"""A module that tests for exact same object"""


def is_same_class(obj, a_class):
    """returns ``True`` if the object is exactly an instance
    of the specified class, othewise ``False``."""

    return isinstance(obj, a_class)
