#!/usr/bin/env python3
"""This module implements LFU caching"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """This class removes data using LRU Algorithm"""

    def __init__(self):
        """Instance initialiser"""
        super().__init__()
        self.recents = []

    def put(self, key, item):
        """This method assigns Item to Key and removes the
        least frequently used item if limit reached
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.recents.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = self.least_used(self.recents)
                print(f"DISCARD: {to_remove}")
                self.cache_data.pop(to_remove)

                

    def get(self, key):
        """Returns value of Key and adds it to recents"""
        self.recents.append(key)
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None

    def least_used(items: list):
        """This returns the least frequent item in list"""
        return min(set(items), key = items.count)
