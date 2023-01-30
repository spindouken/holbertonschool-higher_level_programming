#!/usr/bin/python3
"""
Based module contains based class Base
Based class Base contains private class '__nb_objects'
    that keeps track of the number of instances created
    and a public instance attribute 'id' that is either
    assigned or auto-generated based
    on the '__nb_objects' attribute.
    Also, contains class constructor __init__.
"""
import json


class Base:
    """
    class Base is based
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize id, increment class attribute if no id
            and set id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
