#!/usr/bin/python3
"""
100-github_commits.py
Module that lists the last 10 commits made on a GIT Repository
"""

import requests
from sys import argv

if __name__ == "__main__":
    github_commits = "https://api.github.com/repos/{}/{}/commits"
    r = requests.get(github_commits.format(argv[2], argv[1]))
    obj_json = r.json()
    i = 1
    for obj in obj_json:
        if i <= 10:
            print(r.get('sha') + ': ', end="")
            print(r.get('commit').get('author').get('name'))
        else:
            break
        i += 1
