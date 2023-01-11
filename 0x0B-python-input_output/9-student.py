#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Instantiation

        Args:
            first_name (str): first name of a student.
            last_name (str): last name of a student.
            age (int): age of a student.

        Returns:
            Dictionary representation.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
