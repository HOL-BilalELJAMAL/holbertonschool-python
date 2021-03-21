#!/usr/bin/env python3
"""
web.py
Module used for expiring web cache and tracker
"""


import requests
from functools import wraps
import redis
from typing import Callable


red = redis.Redis()
red.flushdb()


def my_cache(method: Callable) -> Callable:
    """
    Callable function for counting how many times a request
    has been made
    """
    @wraps(method)
    def wrap(*args, **kwargs):
        """Function wrapper of decorator"""
        url = args[0]
        text = red.get(url)
        if text is None:
            text = method(*args, **kwargs)
            if text is not None:
                red.setex(url, 10, text)
                red.incr("count:"+url)
        else:
            text = text
            red.incr("count:"+url)
        return text
    return wrap


@my_cache
def get_url(url: str) -> bytes:
    """
    Function that returns how many times a particular URL was
    access
    """
    try:
        text = requests.get(url).content
        return text
    except Exception:
        return None


def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    access
    """
    return get_url(url)
