#!/usr/bin/python3
"""Inherit list"""


class MyList(list):
    """MyList class inherits list"""

    def print_sorted(self):
        """prints the list, but sorted(ascending sort)"""

        print(sorted(self))
