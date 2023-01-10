#!/usr/bin/python3
"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Represents a BaseGeometry class"""

    def area(self):
        """Raises an Exception"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""

        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')


class Rectangle(BaseGeometry):
    """Rectangle inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation

        Args:
            width (int): Width of a rectangle
            height (int): Height of a rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
