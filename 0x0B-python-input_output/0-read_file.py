#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Opens and reads a file"""

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
