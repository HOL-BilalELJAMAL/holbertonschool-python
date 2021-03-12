#!/usr/bin/python3
"""
0-count.py
Module that defines a recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list, dic={}, after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords

    Args:
        subreddit (str): Subreddit to search
        word_list (list): List of words to search
        dic (dict): Pairs of words - counts
        after (str): Parameter for the next page of the API result
    """
    if len(dic) == 0:
        for word in word_list:
            dic[word] = 0
    try:
        u = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
        h = {'User-Agent': 'test'}
        p = {'limit': 100}
        if after:
            p['after'] = after
        r = requests.get(u, headers=h, params=p, allow_redirects=False).json()
        posts = r.get('data').get('children')
        for x in posts:
            for word in word_list:
                if word.lower() in x.get('data').get('title').lower().split():
                    dic[word] += 1
        after = r.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, dic, after)
        for k, v in sorted(dic.items(), key=lambda x: x[1], reverse=True):
            if v > 0:
                print('{}: {}'.format(k, v))
    except:
        return
