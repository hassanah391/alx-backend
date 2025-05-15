#!/usr/bin/env python3
"""BasicCache module: Implements a basic caching system with no limit."""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A basic cache that inherits from BaseCaching
        and does not have a limit."""
    def put(self, key, item):
        """Add an item in the cache.

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key from the cache.

        Args:
            key: The key of the item to retrieve.
        Returns:
            The item if found, else None.
        """
        if key is None or key not in self.cache_data.keys():
            return None

        return self.cache_data[key]
