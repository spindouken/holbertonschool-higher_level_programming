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
    content_type = response.headers.get('content-type')
    response_body = response.text
    print("Body response:")
    print(f"\t- type: {content_type}")
    print(f"\t- content: {response_body}")


if __name__ == "__main__":
    main()
