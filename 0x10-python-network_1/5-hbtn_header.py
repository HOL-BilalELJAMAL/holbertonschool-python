#!/usr/bin/python3
"""
5-hbtn_header.py
Module that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
