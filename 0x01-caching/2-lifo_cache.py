#!/usr/bin/env python3
"""This module implements LIFO caching"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """This class removes data using LIFO Algorithm"""

    def __init__(self):
        """Instance initialiser"""
        super().__init__()

    def put(self, key, item):
        """This method assigns Item to Key
        And removes the last item if out of range
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if not len(self.cache_data) > BaseCaching.MAX_ITEMS:
                copy = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                copy = list(self.cache_data.keys())
                last_item = key if copy.count(key) > 1 else copy[-2]
                print(f"DISCARD: {last_item}")
                del self.cache_data[last_item]

    def get(self, key):
        """Returns value of Key"""
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None


my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()