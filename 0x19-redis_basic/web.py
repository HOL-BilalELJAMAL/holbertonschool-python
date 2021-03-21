#!/usr/bin/env python3
"""
web.py
Module used for expiring web cache and tracker
"""

from functools import wraps
import redis
import requests
from typing import Callable


def count(method: Callable):
    """
    Callable function for counting how many times a request
    has been made
    """
    r = redis.Redis()

    @wraps(method)
    def wrapper(url):
        """Function wrapper of decorator"""
        print(type(method(url)))
        try:
            r.incr(f"count:{url}")
            expiration_count = r.get(f"cached:{url}")
            if expiration_count:
                return expiration_count.decode('utf-8')

            html = method(url)
            r.setex(f"cached:{url}", 10, html)
            return html
        except:
            return ""

    return wrapper


@count
def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    accessed in the key
    """
    response = requests.get(url)
    return response.text
