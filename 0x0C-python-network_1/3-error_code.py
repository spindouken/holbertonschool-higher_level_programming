#!/usr/bin/python3
"""Sends a request to a URL and displays the body
of the response (decoded in utf-8).

This script takes in a URL as a command-line argument and sends a request
to the URL using the urllib package.
It then decodes the response body in utf-8 and displays it to the user.
If the response raises an HTTPError, the script catches the exception
and prints the error code.
"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            page = response.read()
            print("{}".format(page.decode('utf-8')))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
