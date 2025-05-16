#!/usr/bin/python3
""" Module 4-mru_cache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.access_order = []

    def put(self, key, item):
        """Add item to cache"""
        if key is None or item is None:
            return

        # If key already exists, just update its position later
        if key in self.cache_data:
            self.access_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Evict the most recently used (last in the list)
            mru_key = self.access_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        # Add/Update the key and mark as most recently used
        self.cache_data[key] = item
        self.access_order.append(key)

    def get(self, key):
        """Get item from cache"""
        if key is None or key not in self.cache_data:
            return None

        # Update access order (move to end)
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
