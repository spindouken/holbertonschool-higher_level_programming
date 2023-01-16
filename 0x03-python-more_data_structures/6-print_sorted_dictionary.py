#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for da_key in sorted(a_dictionary):
        print(f"{da_key}: {a_dictionary[da_key]}")
