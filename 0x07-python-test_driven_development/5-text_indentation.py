#!/usr/bin/python3
"""A module that print a text"""


def text_indentation(text):
    """A function that prints a text with two new lines after
        these . ? : characters.

        Args:
            text(str): a text

        Raise:
            TypeError: if text is not a string
        """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    flag = 0
    for char in text:
        if flag == 0 and char == " ":
            continue
        else:
            flag = 1
        if flag == 1:
            if char == '?' or char == '.' or char == ':':
                print(char)
                print()
                flag = 0
            else:
                print(f"{char}", end="")
