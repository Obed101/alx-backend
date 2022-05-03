#!/usr/bin/env python3
"""This module implements FIFO caching"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """This class removes data using FIFO Algorithm"""

    def __init__(self):
        """Instance initialiser"""
        super().__init__()

    def put(self, key, item):
        """This method assigns Item to Key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # First item is the first key
                first_item = list(self.cache_data.keys())[0]
                print(f"DISCARD: {first_item}")
                del self.cache_data[first_item]

    def get(self, key):
        """Returns value of Key"""
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None
