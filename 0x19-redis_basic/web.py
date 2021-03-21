#!/usr/bin/env python3
"""
web.py
Module used for expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """Callable function decorator wrapper"""

    @wraps(fn)
    def wrapper(url):
        """Function wrapper of decorator"""
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result

    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """
    Function that returns how many times a particular URL was
    accessed in the key
    """
    response = requests.get(url)
    return response.text
