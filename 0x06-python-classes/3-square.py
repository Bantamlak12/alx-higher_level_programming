#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): Size of a square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=  0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
