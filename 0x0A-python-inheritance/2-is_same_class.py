#!/usr/bin/python3
"check if object shares the same class"

def is_same_class(obj, a_class):
    """returns true if the object shares the same instance of the specified class
    Return false if different instance"""

    return type(obj) is a_class
