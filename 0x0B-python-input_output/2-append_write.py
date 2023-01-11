#!/usr/bin/python3
"""Appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Writes a string to text file.

    Args:
        filename (str): name of a file.
        text (str): text to be appended to the filename.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding='utf-8') as a_file:
        return a_file.write(text)
