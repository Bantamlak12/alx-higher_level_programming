#!/usr/bin/python3
"""Defines a module square that inherits from rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a new Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiation.

        Args:
            size (int): size of the square
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): identity of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter of size"""
        self.width = value
        self.height = value

    def __str__(self):
        """ returns the square in form: [Square] (<id>) <x>/<y> - <size>"""

        desc = "[{}] ({}) {}/{} - {}".format(__class__.__name__, self.id,
                                             self.x, self.y, self.size)
        return desc

    def update(self, *args, **kwargs):
        """updates the square class:

        Args:
            *args (int): is the list of arguments - no-keyworded arguments
                    1st argument should be the id attribute
                    2nd argument should be the size attribute
                    3rd argument should be the x attribute
                    4th argument should be the y attribute
            **kwargs (dict): key/value paires(keyworded arguments)
        """
        i = 0
        if len(args) != 0:
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i = i + 1
        elif len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """update the class with its dictionary representation"""

        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
            }
