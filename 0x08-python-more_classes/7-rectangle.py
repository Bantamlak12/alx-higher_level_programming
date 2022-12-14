#!/usr/bin/python3
"""A module that defines a rectangle"""


class Rectangle:
    """Represents a rectang.

    Attributes:
        number_of_instances (int): number objects.
        print_symbole (any): is used to represent a string.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Instantation with width and height"""

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property   # getter
    def width(self):
        return self.__width

    @width.setter   # setter
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

    def __str__(self):
        """Print a rectangle with the character #"""

        if self.__width == 0 or self.__height == 0:
            return ""

        r = []
        for h in range(self.__height):
            for w in range(self.__width):
                r.append(str(self.print_symbol))
            if h != self.__height - 1:
                r.append('\n')
        return ("".join(r))

    def __repr__(self):
        """return a string representation of the rectangle to be able to
        recreate a new instance"""

        return ('Rectangle({}, {})'.format(self.__width, self.__height))

    def __del__(self):
        """print a message 'Bye rectangle' when an instance of a 'Rectangle'
        is deleted"""

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
