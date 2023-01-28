#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class
    Attributes:
        first_name (str): first name of student
        last_name (str): last name of student
        age (int): age of student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize a student class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        ...if 'attributes' is passed, only includes attributes in dict
            that are present in the 'attributes' list
        Variables:
            attributes: a list of strings to be used as arguments
            newDictionary: version of dictionary which only contains the
                attributes contained in 'attributes' argument list
            __dict__ : dictionary containing all
                attributes of the "Student" object
            element: variable used to itterate through 'attributes' list passed
                to 'to_json' method. In each iteration, takes value of the new
                element in list. This is to check whether the element is
                presentin the __dict__ of the "Student" class object.
        """

        newDictionary = {}
        if attributes is None:
            return self.__dict__
        for element in attributes:
            if element in self.__dict__:
                newDictionary[element] = self.__dict__[element]
        return newDictionary

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        Student class public attributes: first_name, last_name, age
        key: public attribute name
        value: dictionary value of the public attribute
        """

        for key, value in json.items():
            setattr(self, key, value)
