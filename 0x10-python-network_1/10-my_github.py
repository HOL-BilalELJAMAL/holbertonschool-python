#!/usr/bin/python3
"""
10-my_github.py
Module that takes your GitHub credentials (username and password) and uses
the GitHub API to display your id
"""

import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get("id"))
