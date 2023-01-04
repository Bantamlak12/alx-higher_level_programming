#!/usr/bin/python3
"""Defines a 101-locked module"""


class LockedClass(object):
    """
    This class prevents the user from dynamically creating new instance
    attributes, except the new instance attribute is called first_name.
    """
    __slots__ = ('first_name')
