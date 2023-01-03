#!/usr/bin/python3
"""A module that prints a full name"""


def say_my_name(first_name, last_name=""):
    """A function that prints a full name

    Args:
        first_name (str): first name of a person
        last_name (str): last name of a person

    Raise: TypeError exception if first name or last name is not string.

    Return: A full name with a message 'My name is <first name> <last name>'
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    full_name = first_name.strip().title() + " " + last_name.strip().title()

    print(f"My name is {full_name}")
