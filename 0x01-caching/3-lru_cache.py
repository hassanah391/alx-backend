#!/usr/bin/python3
""" Module 3-lru_cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add item to cache"""
        if key is None or item is None:
            return

        # If key is already in cache, remove it to update its position later
        if key in self.cache_data:
            self.access_order.remove(key)

        self.cache_data[key] = item
        self.access_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Pop the least recently used (first in the list)
            lru_key = self.access_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update access order (move to end)
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
