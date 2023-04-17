#!/usr/bin/python3

"""Defines class Base"""


class Base:
    """Represent base model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base
        Args:
            id (int): identity of new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries []:
            return []
        else:
            return json.dumps(list_dictionaries)

