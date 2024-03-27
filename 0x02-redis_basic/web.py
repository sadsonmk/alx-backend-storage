#!/usr/bin/env python3
"""This modules caches the request module results"""

import redis
import requests
from typing import Callable
from functools import wrap


def track_url(func: Callable) -> Callable:
    """decorator to track urls for the get_page"""
    @wraps(func)
    def wrapper(url: str) -> str:
        r = redis.Redis()
        r.incr(f'count:{url}')
        page = r.get(f'{url}')
        if page:
            return page.decode("utf-8")
        result = func(url)
        r.set(f'{url}', result, 10)
        return result
    return wrapper


@track_url
def get_page(url: str) -> str:
    """obtains the HTML content of a particular URL and returns it"""
    response = requests.get(url)
    return response.text
