#!/usr/bin/python3
"""
103-search_twitter.py
Module that displays the first 5 tweets based on specific search result
using this format [<Tweet ID>] <Tweet text> by <Tweet owner name>
"""

import requests
import base64
import sys

client_key = sys.argv[1]
client_secret = sys.argv[2]
search_str = sys.argv[3]
