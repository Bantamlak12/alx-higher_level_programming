#!/usr/bin/python3
"""Afunction that writes a string to text file"""


def write_file(filename="", text=""):
    """Writes a string to text file.

    Args:
        filename (str): name of a file.
        text (str): text to be written to the filename.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
