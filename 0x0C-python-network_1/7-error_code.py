#!/usr/bin/python3
"""Sends a GET request to a URL and displays
the body of the response decoded in UTF-8"""
import requests
from sys import argv


if __name__ == "__main__":
    # Check if a URL was provided as a command line argument
    page = requests.get(argv[1])
    if page.status_code >= 400:
        print("Error code: {}".format(page.status_code))
    else:
        print(page.text)
