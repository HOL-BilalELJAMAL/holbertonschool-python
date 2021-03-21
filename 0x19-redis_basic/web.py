#!/usr/bin/env python3
"""
web.py
Module used for expiring web cache and tracker
"""

from functools import wraps
import redis
import requests
from typing import Callable

r = redis.Redis()


def count_requests(method: Callable) -> Callable:
    """
    Callable function for counting how many times a request
    has been made
    """

    @wraps(method)
    def wrapper(url):
        """Function wrapper of decorator"""
        r.incr(f"count:{url}")
        cached_html = r.get(f"cached:{url}")
        if cached_html:
            return cached_html.decode('utf-8')

        html = method(url)
        r.setex(f"cached:{url}", 10, html)
        return html

    return wrapper


@count_requests
def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    accessed in the key
    """
    response = requests.get(url)
    return response.text
