#!/usr/bin/python3
"""A module that prints a square"""


def print_square(size):
    """A function that prints a square with the character #.

    Args:
        size (int): size length of the square.

    Raise:
        TypeError: if size is not integer
                   if size is a float and less than 0

        ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float) or size < 0:
        raise TypeError('size must be an integer')

    for i in range(size):
        for j in range(size):
            print('#', end="")
        print()
