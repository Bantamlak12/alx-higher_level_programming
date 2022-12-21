#!/usr/bin/python3
"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square

        Args:
            size (int): Size of a square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """getter"""
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=  0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """setter"""
        if (not isinstance(value, tuple) or not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the area"""
        return self.__size ** 2

    def my_print(self):
        """prints a square hash"""
        if self.__size == 0:
            print("")
        else:
            print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for k in range(self.__size):
                    print("#", end="")
                print("")
