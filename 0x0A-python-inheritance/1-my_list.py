#!/usr/bin/python3
"""A module that defines a class MyList that inherits from list."""

class MyList(list):
    def print_sorted(self):
        print(sorted(self))
