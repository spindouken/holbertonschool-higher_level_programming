#!/usr/bin/python3
"""Sends a POST request to a URL with an
email as a parameter and prints the response"""
import requests
from sys import argv


if __name__ == "__main__":
    page = requests.get(argv[1])
    print(page.headers.get('X-Request-Id'))
