#!/usr/bin/python3
"""Defines a Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        Returns:
            Area of the rectangle, and rectangle discription
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of the rectangle"""

        return self.__width * self.__height

    def __str__(self):
        """print() prints, and str() returns"""

        string = "[" + self.__class__.__name__ + "] "
        string += str(self.__width) + "/" + str(self.__height)

        return string
