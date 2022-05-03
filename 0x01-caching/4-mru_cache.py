#!/usr/bin/env python3
"""This module implements LRU caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """This class removes data using MRU Algorithm"""

    def __init__(self):
        """Instance initialiser"""
        super().__init__()
        self.recents = []

    def put(self, key, item):
        """This method assigns Item to Key and removes the
        Most recently used item if out of range
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.recents.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                to_remove = self.recents[-2]
                print(f"DISCARD: {to_remove}")
                try:
                    self.cache_data.pop(to_remove)
                except KeyError:
                    self.cache_data.pop(self.recents[1])
                    del self.recents[-2]

    def get(self, key):
        """Returns value of Key and adds it to recents"""
        self.recents.append(key)
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None
