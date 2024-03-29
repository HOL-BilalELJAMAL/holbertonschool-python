#!/usr/bin/python3
"""
0-count.py
Module that defines a recursive function that queries the Reddit API
"""

from collections import Counter, defaultdict
import re
import requests


def count_words(subreddit, word_list, res=defaultdict(int), after=None):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords

    Args:
        subreddit (str): Subreddit to search
        word_list (list): List of words to search
        res (dict): Pairs of words - counts
        after (str): Parameter for the next page of the API result
    """
    agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)\
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132i\
            Safari/537.36"
    headers = {"User-Agent": agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        req = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = req.get('data').get('children')
        for title in titles:
            count = Counter(title.get('data').get('title').lower().split(' '))
            for x in word_list:
                if x.lower() in count:
                    res[x] += count.get(x.lower())
        after = req.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, res, after)
        sort_first = sorted(res.items(), key=lambda x: x[0])
        for k, v in sorted(sort_first, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))
    except:
        return
