#!/usr/bin/env python3
"""ALX SE"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """A LIFO caching system"""
    def __init__(self):
        """Initialize the class"""
        self.i = 2
        self.keys = []
        super().__init__()

    def put(self, key, item):
        """Add an item in a cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        self.keys.append(key)
        if len(self.keys) != len(self.cache_data):
            self.keys.pop()

        if len(self.cache_data) > super().MAX_ITEMS:
            if self.i > 3:
                self.i = 2
            print(f"DISCARD: {self.keys[-self.i]}")
            del self.cache_data[self.keys[-self.i]]
            self.keys.pop(-self.i)
            self.i += 1

    def get(self, key):
        """Get an item by key"""
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data[key]
