#!/usr/bin/python3
"""
0-hbtn_status.py
Module that fetches https://intranet.hbtn.io/status
"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    status_str = "Body Response:\n"
    status_str += "\t-type: " + str(type(html)) + "\n"
    status_str += "\t-content: " + str(html) + "\n"
    status_str += "\t-utf8 content: " + str(html.decode('utf-8'))
    print(status_str)
