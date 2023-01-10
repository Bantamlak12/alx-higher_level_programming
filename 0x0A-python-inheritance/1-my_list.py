#!/usr/bin/python3
"""A module that defines a class MyList that inherits from list."""


class MyList(list):
    """Represents a class MyList"""

    def print_sorted(self):
        """prints the list sorted"""

        print(sorted(self))
