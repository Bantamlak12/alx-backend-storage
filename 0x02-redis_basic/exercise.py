#!/usr/bin/env python3
"""
File: exercise.py

Writing a string to Redis
"""
import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Writing strings to Redis """
    def __init__(self):
        """
        Stores an instance of the Redis client as a private
        variable named _redis.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        parameters:
        - data (Union[str, bytes, int, float]): A value to the key.

        Returns: 
        - (str): Returns the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) \
            -> Union[str, bytes, int, float]:
        """
        parameters:
        - key (str): The key used to retrieve data
        - fn (Collable): Optional collable, used to convert data back to the
        desired format.

        Returns:
        - Union[str, bytes, int, float]: The retrived data
        """
        data = self._redis.get(key)
        if data is None:
            return data
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, bytes, int, float]:
        """
        parameters:
        - key (str): The key used to retrieve data

        Returns:
        - Union[str, bytes, int, float]: The retrived data
        """
        return self.get(key, fu=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Union[str, bytes, int, float]:
        """
        parameters:
        - key (str): The key used to retrieve data

        Returns:
        - Union[str, bytes, int, float]: The retrived data
        """
        return self.get(key, fu=int)


# cache = Cache()

# TEST_CASE = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASE.items():
#     key = cache.store(value)
#     assert cache.get(key, fn=fn) == value
