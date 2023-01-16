#!/usr/bin/python3
"""Defines a module rectangle that inherits from Base."""
from models.base import Base


class Rectangle(Base):
    """Represents a new Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
            x (int): x coordinate of the rectangle
            y (int): y coordinate of the rectangle
            id (int): identity of the rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """getter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """getter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter of x"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """getter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of y"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Defines area of a rectangle"""

        return self.__width * self.__height

    def display(self):
        """Displays a rectangle with '#' in stdout"""

        for y in range(self.y):
            print("")
        for height in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns class Rectangle in the format:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """

        desc = "[{}] ({}) {}/{} - {}/{}".format(__class__.__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)
        return desc

    def update(self, *args, **kwargs):
        """Update class Rectangle.

        Args:
            *args (int): is the list of arguments - no-keyworded arguments
                    1st argument should be the id attribute
                    2nd argument should be the width attribute
                    3rd argument should be the height attribute
                    4th argument should be the x attribute
                    5th argument should be the y attribute
            **kwargs (dict): key/value paires(keyworded arguments)
        """
        i = 0
        if len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
                i = i + 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
