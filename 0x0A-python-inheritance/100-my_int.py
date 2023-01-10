#!/usr/bin/python3
"""Defines a class MyInt"""


class MyInt(int):
    """Inverts the operator != and =="""
    def __eq__(self, a_class):
        return type(a_class) == a_class

    def __ne__(self, a_class):
        return type(a_class) != a_class
