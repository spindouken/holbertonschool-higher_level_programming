#!/usr/bin/python3
"""
This script fetches the https://intranet.hbtn.io/status URL and displays
the type and content of the response body.
"""
import requests


def main():
    """
    Sends an HTTP GET request to https://intranet.hbtn.io/status
    and prints the response body type and content.
    """
    response = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))


if __name__ == "__main__":
    main()
