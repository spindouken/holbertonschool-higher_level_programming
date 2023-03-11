#!/usr/bin/python3
"""Script that fetches url"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        hmm = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(hmm)))
        print("\t- content: {}".format(hmm))
        print("\t- utf8 content: {}".format(hmm.decode("utf8")))
