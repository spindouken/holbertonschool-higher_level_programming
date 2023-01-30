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
from os import path


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        new_dictionary_list = []
        file_name = cls.__name__ + ".json"
        if list_objs is not None:
            for element in list_objs:
                new_dictionary_list.append(element.to_dictionary())
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(new_dictionary_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation"""

        if json_string is None or json_string is []:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        else:
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        file_name = cls.__name__ + ".json"
        instance_list = []
        if path.exists(file_name):
            with open(file_name, "r", encoding="utf-8") as f:
                new_dictionary = cls.from_json_string(f.read())
                for instance in new_dictionary:
                    instance_list.append(cls.create(**instance))
                return instance_list
        else:
            return []
