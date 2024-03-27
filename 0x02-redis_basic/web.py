#!/usr/bin/env python3
"""This modules caches the request module results"""

import redis
import requests
from typing import Callable
from functools import wraps


def track_url(func: Callable) -> Callable:
    """decorator to track urls for the get_page"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """A wrapper function for checking caching of a page and tracking"""
        key = f"count:{url}"

        r = redis.Redis()
        page = r.get(key)
        if page:
            return page.decode("utf-8")
        result = func(url)
        r.set(key, result, ex=10)
        r.incr(f'count:{url}')
        return result
    return wrapper


@track_url
def get_page(url: str) -> str:
    """obtains the HTML content of a particular URL and returns it"""
    response = requests.get(url)
    return response.text


url = "http://slowwly.robertomurray.co.uk"
content = get_page(url)
