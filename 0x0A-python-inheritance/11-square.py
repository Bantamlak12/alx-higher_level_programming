#!/usr/bin/python3
"""Defines a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a new square"""

    def __init__(self, size):
        """Instantiation

        Args:
            size (int): size of a square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
