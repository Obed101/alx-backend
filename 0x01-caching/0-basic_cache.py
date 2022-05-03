#!/usr/bin/env python3
"""This module implements basic caching"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """This Class is a chaching system"""
    def __init__(self):
        """Instance Initialiser"""
        super().__init__()
    
    def put(self, key, item):
        """This calls the super put to assign Item value to Key"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Returns value of Key"""
        try:
            return self.cache_data[key] if key else None
        except KeyError:
            return None
