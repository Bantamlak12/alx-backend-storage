#!/usr/bin/env python3
"""
File: web.py

Implements an expiring web cache and tracker
"""
from functools import wraps
from typing import Callable
import requests
import redis
import time

# Expiration time in sec
time_to_expire_s = 10


def cache_result(function: Callable) -> Callable:
    """
    function (Callable)
    """
    @wraps(function)
    def wrapper(url):
        redis_client = redis.Redis()
        key_count = f"count:{url}"
        key_content = f"content: {url}"

        redis_client.incr(key_count)
        cached_content = redis_client.get(key_content)
        if cached_content is not None:
            return cached_content.decode("utf-8")
        else:
            response = function(url)

        redis_client.setex(key_content, time_to_expire_s, response)

        return response
    return wrapper


@cache_result
def get_page(url: str) -> str:
    """
    parameters:
    - url (url): A url to simulate slow response

    Returns:
    - (str): Content of a particular URL.
    """
    response = requests.get(url)
    return response.text


# url = "http://slowwly.robertomurray.co.uk"
# html = get_page(url)
# print(html)

# time.sleep(10)

# html = get_page(url)
# print(html)
