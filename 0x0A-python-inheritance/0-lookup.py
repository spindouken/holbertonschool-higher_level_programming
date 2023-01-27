#!/usr/bin/python3
"""Lookup attributes and methods"""


def lookup(obj):
    """Returns the list of available attributes
    and methods of an object"""

    return list(dir(obj))
