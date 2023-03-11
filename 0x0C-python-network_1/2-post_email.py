#!/usr/bin/python3
"""
Sends a POST request to the passed URL with an email as a parameter
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    # Define the email value to be sent as a parameter
    value = {'email': argv[2]}

    # Encode the value in a way that can be sent via HTTP POST request
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')

    # Create a request object with the URL and encoded data
    req = urllib.request.Request(argv[1], data)

    # Send the request and read the response
    with urllib.request.urlopen(req) as response:
        page = response.read()

        # Print the body of the response as a string in utf-8 format
        print("{}".format(page.decode('utf8')))
