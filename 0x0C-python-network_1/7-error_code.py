#!/usr/bin/python3
"""Sends a GET request to a URL and displays
the body of the response decoded in UTF-8"""
import requests
from sys import argv


def get_url_body(url: str) -> str:
    """
    Sends a GET request to a URL and returns the body of
    the response decoded in UTF-8.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        str: The body of the response, decoded in UTF-8.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    # Check if a URL was provided as a command line argument
    if len(argv) < 2:
        print("Usage: python3 script.py <URL>")
    else:
        url = argv[1]
        # Call the get_url_body function and print the result
        body = get_url_body(url)
        print(body)
