#!/usr/bin/env python3
"""
web.py
Module used for implementing an expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps

rd = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Callable function for counting how many times a request
    has been made
    """

    @wraps(method)
    def wrapper(url):
        """Function wrapper of decorator"""
        rd.incr(f"count:{url}")
        cached_html = rd.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        rd.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    accessed in the key
    """
    req = requests.get(url)
    return req.text
