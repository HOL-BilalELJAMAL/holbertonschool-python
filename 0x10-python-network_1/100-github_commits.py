#!/usr/bin/python3
"""
100-github_commits.py
Module that lists the first 10 commits made on a GIT Repository
"""

import requests
from sys import argv

if __name__ == "__main__":
    git_api_url = "https://api.github.com/repos/{}/{}/commits"
    response = requests.get(git_api_url.format(argv[2], argv[1]))
    obj_json = response.json()[:10]
    for obj in obj_json:
        print("{}: {}".format(obj.get('sha'),
                              obj.get('commit').get('author').get('name')))
