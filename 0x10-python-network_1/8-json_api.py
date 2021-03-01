#!/usr/bin/python3
"""
8-json_api.py
Module that takes in a letter and sends a POST request with the letter as a
parameter to http://0.0.0.0:5000/search_user
"""

import requests
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = argv[1] if len(argv) == 2 else ""
    response = requests.post(url, data={"q": letter})
    try:
        obj = response.json()
        if obj:
            print("[{}] {}".format(obj.get("id"), obj.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
