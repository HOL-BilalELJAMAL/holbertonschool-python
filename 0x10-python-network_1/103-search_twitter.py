#!/usr/bin/python3
"""
103-search_twitter.py
Module that displays the first 5 tweets based on specific search result
using this format [<Tweet ID>] <Tweet text> by <Tweet owner name>
"""

import requests
import base64
from sys import argv

if __name__ == "__main__":
    client_key = argv[1]
    client_secret = argv[2]
    search_str = argv[3]

    key_secret = '{}:{}'.format(client_key, client_secret).encode('ascii')

    b64_encoded_key = base64.b64encode(key_secret)
    b64_encoded_key = b64_encoded_key.decode('ascii')

    base_url = 'https://api.twitter.com/'
    auth_url = '{}oauth2/token'.format(base_url)
    auth_headers = {
        'Authorization': 'Basic {}'.format(b64_encoded_key),
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    }
    auth_data = {
        'grant_type': 'client_credentials'
    }
    auth_resp = requests.post(auth_url, headers=auth_headers, data=auth_data)

    access_token = auth_resp.json()['access_token']

    search_headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }

    search_params = {
        'q': search_str
    }

    search_url = '{}1.1/search/tweets.json'.format(base_url)
    search_resp = requests.get(search_url, headers=search_headers,
                               params=search_params)

    data = search_resp.json().get('statuses')

    if data:
        n = 0
        for tweet in data:
            if n == 5:
                break
            try:
                print("[{}] {} by {}".format(tweet.get('id'),
                                             tweet.get('text'),
                                             tweet.get('user').get('name')))
                n += 1
            except:
                pass
