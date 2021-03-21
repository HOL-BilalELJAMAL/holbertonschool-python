#!/usr/bin/env python3
"""
web.py
Module used for expiring web cache and tracker
"""

from redis.client import Redis
import requests

redis = Redis()
count = 0


def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    access
    """
    key = f"count:{url}"
    redis.set(key, count)
    resp = requests.get(url)
    redis.incr(key)
    redis.setex(key, 10, redis.get(key))
    return resp.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
