#!/usr/bin/python3
"""
2-post_email.py
Module that takes in a URL and an email, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
(decoded in utf-8)
"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('ascii')
    with urllib.request.urlopen(argv[1], data) as f:
        print(f.read().decode('utf-8'))
