#!/usr/bin/python3
"""
0-count.py
Module that defines a recursive function that queries the Reddit API
"""

from collections import Counter, defaultdict
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
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
            "AppleWebKit/537.36 (KHTML, like Gecko) " \
            "Chrome/89.0.4389.82 Safari/537.36"
    headers = {"User-Agent": agent}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    if after:
        url += '?after={}'.format(after)
    try:
        r = requests.get(url, headers=headers, allow_redirects=False).json()
        titles = r.get('data').get('children')
        for t in titles:
            c = Counter(t.get('data').get('title').lower().split(' '))
            for word in word_list:
                if word.lower() in c:
                    res[word] += c.get(word.lower())
        after = r.get('data').get('after')
        if after:
            return count_words(subreddit, word_list, res, after)
        first_sort = sorted(res.items(), key=lambda x: x[0])
        for k, v in sorted(first_sort, key=lambda x: x[1], reverse=True):
            print('{}: {}'.format(k, v))
    except:
        return
