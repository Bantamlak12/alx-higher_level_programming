#!/usr/bin/python3
"""A module that adds two integers

   a and b must be integers or float, otherwise raise TypeError exception
   with the message 'a must be an integer' or 'b must be an integer'
"""


def add_integer(a, b=98):
    """Integer addition

    Args:
        a: integer or float number
        b: integer or float number

    Return:
        the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
