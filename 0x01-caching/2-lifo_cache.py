#!/usr/bin/python3
"""2-lifo_cache module: Implements a LIFO
    (Last-In, First-Out) caching system."""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache defines a caching system with LIFO eviction policy."""
    def put(self, key, item):
        """Add an item in the cache using LIFO eviction policy.

        If the cache is at its maximum capacity, discard the most
        recently added item (last in) before inserting the new one.
        If either key or item is None, do nothing.
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= self.MAX_ITEMS \
                and key not in self.cache_data:
            recent_item = self.cache_data.popitem()
            print("DISCARD: {}".format(recent_item[0]))

        # delete an exist key and then put in top
        # to update this key in a FIFO concept (stack)
        if key in self.cache_data:
            del self.cache_data[key]
            self.cache_data[key] = item
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
