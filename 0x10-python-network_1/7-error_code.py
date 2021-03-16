#!/usr/bin/python3
"""
7-error_code.py
Module that that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print("Error code: " + str(response.status_code)) \
        if response.status_code >= 400 \
        else print(response.text)
