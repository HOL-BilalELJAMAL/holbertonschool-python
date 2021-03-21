#!/usr/bin/env python3
"""
exercise.py
Module that defines a Cache and returns Cache redis including:
    - Writing strings to Redis
    - Reading from Redis and recovering original type
    - Incrementing values
    - Storing lists
    - Retrieving lists
"""

import redis
from uuid import uuid4
from typing import Union, Optional, Callable
from functools import wraps

# Redis storage types
UnionOfTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """
    Callable functions that returns the number of calls
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Function wrapper of decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Callable function that returns the number of history inputs
    """
    inputs = method.__qualname__ + ":inputs"
    outputs = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """Function wrapper of decorator"""
        self._redis.rpush(inputs, str(args))
        returned_method = method(self, *args, **kwds)
        self._redis.rpush(outputs, str(returned_method))
        return returned_method
    return wrapper


def replay(method: Callable):
    """
    Callable function that displays the calls history
    """
    self_ = method.__self__
    stored_name = method.__qualname__
    stored_key = self_.get(stored_name)
    if stored_key:
        times = self_.get_str(stored_key)
        inputs = self_._redis.lrange(stored_name + ":inputs", 0, -1)
        outputs = self_._redis.lrange(stored_name + ":outputs", 0, -1)

        print(f"{stored_name} was called {times} times:")
        zipvalues = zip(inputs, outputs)
        result_list = list(zipvalues)
        for k, v in result_list:
            name = self_.get_str(k)
            val = self_.get_str(v)
            print(f"{stored_name}(*{name}) -> {val}")


class Cache:
    """
    Represents a class called Cache with a protected instance
    attribute called redis
    """

    def __init__(self):
        """Initialization of the protected instance attribute"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: UnionOfTypes) -> str:
        """Function that stores data into redis cache"""
        key = str(uuid4())

        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> UnionOfTypes:
        """Function that gets key from redis"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self, string: bytes) -> str:
        """Function that gets the string value of an object"""
        return string.decode("utf-8")

    def get_int(self, number: int) -> int:
        """Function that gets the int value of an object"""
        result = 0 * 256 + int(number)
        return result
