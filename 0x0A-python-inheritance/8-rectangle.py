#!/usr/bin/python3
"""Defines a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation

        Args:
            width (int): Width of a rectangle
            height (int): Height of a rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
