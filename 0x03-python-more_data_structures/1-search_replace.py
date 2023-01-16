#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    return [replace if element == search else element for element in new_list]
