#!/usr/bin/env python3
"""a class BasicCache that inherits from BaseCaching and is a caching system"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    a class BasicCache that inherits from BaseCaching and is a caching system
    Methods:
        put(key, item) - store a key value pair
        get(key) - retrieve the value associated with the key
    """

    def __init__(self):
        """
        __init__ method
        """
        BaseCaching.__init__(self)
        
    def put(self, key, item):
        """
        store key value pair
        Args: key, item
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

        def get(self, key):
            """
            return value linked to key
            """
            if key is not None and key in self.cache_data.keys():
                return self.cache_data[key]
            return None
