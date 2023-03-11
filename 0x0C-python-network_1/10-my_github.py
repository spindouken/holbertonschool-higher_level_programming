#!/usr/bin/python3

"""Script that takes GitHub credentials and uses GitHub API to display user ID"""

import requests
from sys import argv


def get_user_id(username: str, password: str) -> int:
    """
    Sends a GET request to the GitHub API using the provided credentials to retrieve
    the authenticated user's ID.

    Args:
        username (str): The username of the GitHub account.
        password (str): The password or personal access token of the GitHub account.

    Returns:
        int: The ID of the authenticated user.
    """
    response = requests.get('https://api.github.com/user', auth=(username, password))
    data = response.json()
    return data.get('id')


if __name__ == "__main__":
    # Check if credentials were provided as command line arguments
    if len(argv) != 3:
        print("Usage: python3 script.py <username> <password>")
    else:
        username, password = argv[1], argv[2]
        user_id = get_user_id(username, password)
        print(user_id)
