#!/usr/bin/python3
"""Sends a POST request to a URL with a search query as a parameter
and prints the ID and name of the resulting user"""
import requests
from sys import argv


def search_user(query: str) -> str:
    """
    Sends a POST request to a specific URL with a search query as a parameter.
    If the response contains a valid JSON object with an 'id' and 'name' field,
    returns a string with the ID and
    name of the resulting user. If the response
    contains an empty list, returns 'No result'.
    Otherwise, returns 'Not a valid JSON'.

    Args:
        query (str): The search query to be sent in the POST request.

    Returns:
        str: A string containing the ID
        and name of the resulting user, or a message indicating
        that no results were found or that the response
        was not a valid JSON object.
    """
    url = "http://0.0.0.0:5000/search_user"
    query_params = {"q": query}
    response = requests.post(url, query_params)
    try:
        json_response = response.json()
        if len(json_response) == 0:
            return "No result"
        else:
            return "[{}] {}".format(json_response.get('id'),
                                    json_response.get('name'))
    except ValueError:
        return "Not a valid JSON"


if __name__ == "__main__":
    # Check if a search query was provided as a command line argument
    if len(argv) < 2:
        query = ""
    else:
        query = argv[1]
    # Call the search_user function and print the result
    result = search_user(query)
    print(result)
