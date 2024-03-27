#!/usr/bin/env python3
"""This is a module for creating a Cache class. In the __init__
    method, store an instance of the Redis client as a private
    variable named _redis (using redis.Redis()) and flush the
    instance using flushdb
"""

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def call_history(method: Callable) -> Callable:
    """uses rpush to create a list of inputs and outputs"""

    inputs = f'{method.__qualname__}:inputs'
    outputs = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(inputs, str(args))
        output = method(self, *args)
        self._redis.rpush(outputs, output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """a decorator that counts the number of times a method is called"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    """a cache class that stores an instance of the Redis
    client as a private variable named _redis
    """
    def __init__(self):
        """initializes a redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key (e.g. using uuid), store
        the input data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Optional[any]:
        """takes a key string argument and an optional Callable argument
        named fn. This callable will be used to convert the data back to
        the desired format.
        """
        result = self._redis.get(key)
        if result is None:
            return None
        if fn:
            return fn(result)
        return result

    def get_str(self, key: str) -> Optional[str]:
        """Retrievse a value from the cache class as a string"""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieves a value from the cache as an integer"""
        return self.get(key, int)
