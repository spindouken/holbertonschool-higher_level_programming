#!/usr/bin/python3
"""Sends a POST request to a URL with an email as a parameter and prints
the response"""
import requests
from sys import argv


def post_email(url: str, email: str) -> str:
    """Sends a POST request to a URL with an email as a parameter and returns
    the response as a string.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include as a parameter in the
            request.

    Returns:
        str: The response from the server as a string.
    """
    params_to_post = {'email': email}
    response = requests.post(url, params_to_post)
    return response.text


if __name__ == "__main__":
    # Check if a URL and email address were provided as command line arguments
    if len(argv) < 3:
        print("Usage: python3 script.py <URL> <email>")
    else:
        url = argv[1]
        email = argv[2]
        # Call the post_email function and print the result
        response_text = post_email(url, email)
        print(response_text)
