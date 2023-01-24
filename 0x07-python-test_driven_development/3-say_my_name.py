#!/usr/bin/python3
"""say_my_name prints: "My name is <first name> <last name>"""


def say_my_name(first_name:str, last_name:str =""):
    """
    This function takes in two string arguments: first_name and last_name, and prints out a string that says "My name is {first_name} {last_name}"
    Args:
        first_name (str): The first name of the person
        last_name (str): The last name of the person
    Raises:
        TypeError: When the first_name or the last_name is not of type string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
