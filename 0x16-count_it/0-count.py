#!/usr/bin/python3
"""
0-count.py
Module that defines a recursive function that queries the Reddit API
"""

import requests


def count_words(subreddit, word_list):
    """
    Auxiliary function that invokes the function alt_count_words

    Args:
        subreddit (str): Subreddit to search
        word_list (list): List of words to search
    """
    instances = {}
    after = ""
    count = 0
    return alt_count_words(subreddit, word_list, instances, after, count)


def alt_count_words(subreddit, word_list, instances={}, after="", count=0):
    """
    Recursive function that queries the Reddit API, parses the title of all
    hot articles, and prints a sorted count of given keywords

    Args:
        subreddit (str): Subreddit to search
        word_list (list): List of words to search
        instances (dict): Pairs of words - counts. (default {})
        after (str): Parameter for the next page of the API result (default "")
        count (int): Number of results matched (default 0)
    """
    url = "https://www.reddit.com/r/" + subreddit + "/hot/.json"
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " \
                 "AppleWebKit/537.36 (KHTML, like Gecko) " \
                 "Chrome/89.0.4389.82 Safari/537.36"
    h = {"User-Agent": user_agent}
    p = {"after": after, "count": count, "limit": 100}
    response = requests.get(url, headers=h, params=p, allow_redirects=False)

    try:
        rj = response.json()
        if response.status_code > 300:
            raise BaseException
    except BaseException:
        return

    rj = rj.get("data")
    after = rj.get("after")
    count += rj.get("dist")
    for child in rj.get("children"):
        title = child.get("data").get("title").lower().split()
        for word in word_list:
            if word.lower() in title:
                t = len([t for t in title if t == word.lower()])
                w = instances.get(word)
                instances[word] = t if w is None else instances[word] + t

    if after is None:
        if len(instances) == 0:
            print("")
            return
        code = []
        for item, value in instances.items():
            code.append((value, item))
        code.sort(reverse=True)
        for k in code:
            item, value = k[0], k[1]
            print("{}: {}".format(value, item))
    else:
        alt_count_words(subreddit, word_list, instances, after, count)
