#!/usr/bin/env python3
"""This module implements LRU caching"""

from asyncio import to_thread
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """This class removes data using LRU Algorithm"""

    def __init__(self):
        """Instance initialiser"""
        super().__init__()
        self.recents = []

    def put(self, key, item):
        """This method assigns Item to Key and removes the
        least recently used item if out of range
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.recents.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = self.recents[0]
                print(f"DISCARD: {to_remove}")
                try:
                    self.cache_data.pop(to_remove)
                except KeyError:
                    self.cache_data.pop(self.recents[1])
                    del self.recents[0]

    def get(self, key):
        """Returns value of Key and adds it to recents"""
        self.recents.append(key)
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None


my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
