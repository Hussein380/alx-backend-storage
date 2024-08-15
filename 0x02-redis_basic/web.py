#!/usr/bin/env python3
'''A module with tools for request caching and tracking.
'''
import redis
import requests
from functools import wraps
from typing import Callable

# Create a Redis instance to be used across the module
redis_store = redis.Redis()
'''The module-level Redis instance for caching request data.
'''

def data_cacher(method: Callable) -> Callable:
    '''Decorator to cache the output of a method that fetches data from a URL.
    
    Args:
        method (Callable): The function to be decorated, which fetches data from a URL.

    Returns:
        Callable: A wrapped function that caches the result of the original function.
    '''
    @wraps(method)
    def invoker(url: str) -> str:
        '''The wrapper function that handles caching.
        
        Args:
            url (str): The URL whose data needs to be fetched and cached.
        
        Returns:
            str: The cached or newly fetched content of the URL.
        '''
        # Increment the request count for the given URL
        redis_store.incr(f'count:{url}')
        
        # Check if the result is already cached
        result = redis_store.get(f'result:{url}')
        if result:
            # Return the cached result if available
            return result.decode('utf-8')
        
        # Fetch the data if not cached
        result = method(url)
        
        # Reset the request count for the URL
        redis_store.set(f'count:{url}', 0)
        
        # Cache the result with an expiration time of 10 seconds
        redis_store.setex(f'result:{url}', 10, result)
        
        return result
    
    return invoker

@data_cacher
def get_page(url: str) -> str:
    '''Fetches and returns the content of a URL.
    
    Uses the `data_cacher` decorator to cache the response and track requests.
    
    Args:
        url (str): The URL to fetch.
    
    Returns:
        str: The content of the URL.
    '''
    # Perform the HTTP GET request and return the page content
    return requests.get(url).text

