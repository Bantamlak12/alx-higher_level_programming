#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Instantation with width and height"""

        self.width = width
        self.height = height

    @property   #getter
    def width(self):
        return self.__width

    @width.setter   #setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Compute and return the area of a rectangle"""

        return self.__height * self.__width

    def perimeter(self):
        """Compute and return the perimeter of a rectangle"""
        
        if self.__height == 0 or self.__width == 0:
            return 0
        return ((self.__height * 2) + (self.__width * 2))
