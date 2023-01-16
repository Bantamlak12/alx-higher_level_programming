#!/usr/bin/python3
"""Defines a module ``base``."""
import json
import csv


class Base:
    """Represents a new class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Instantiation.

        Args:
            id (int): represents id of an object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (dict): is a list of dictionaries

        Returns:
            "[]": If list_dictionaries is None or empty, otherwise
            JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs.

        Args:
            cls: class
            list_objs: is a list of instances who inherits of Base
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding='utf-8') as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("[]")
            else:
                obj_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string(dicts): is a string representing a list of dictionaries

        Returns:
            []: If json_string is None or empty, otherwise
            A list represented by json_string.
        """
        if json_string is None or len(json_string) == 0 or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """An instance with all attributes already set.

        Args:
            cls: class
            **dictionary (dict): key/value pairs
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1, 0, 0)  # dummy instance
        elif cls.__name__ == "Square":
            new = cls(1, 0, 0, 0)  # dummy instance
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        Args:
            cls: class
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                return Base.from_json_string(f.read())
        except json.decoder.JSONDecodeError:
            return []
