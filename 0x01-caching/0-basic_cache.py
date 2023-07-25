#!/usr/bin/python3
"""ALX SE"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """A caching system"""
    def __init__(self):
        """Initialize the class"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
