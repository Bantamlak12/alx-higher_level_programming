#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
            size (int): Size of a square
        """
        self.size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=  0")
        else:
            self.__size = value

    def area(self):
        """return the area"""
        return self.__size ** 2
