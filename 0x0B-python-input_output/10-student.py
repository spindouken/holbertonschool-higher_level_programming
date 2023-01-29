#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Initialize student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
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
        if attrs is None:
            return self.__dict__
        for element in attrs:
            if element in self.__dict__:
                newDictionary[element] = self.__dict__[element]
        return newDictionary
