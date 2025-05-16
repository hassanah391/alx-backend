#!/usr/bin/python3
"""FIFOCache module: Implements a FIFO caching system."""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A FIFO cache that discards the oldest items first
    when the cache exceeds its limit."""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache using FIFO algorithm.

        If the cache exceeds the maximum number of items,
        the oldest item is discarded.

        Args:
            key: The key under which the item is stored.
            item: The item to store in the cache.
        """
        if key is None or item is None:
            return

        # Evict the oldest item if we're about to exceed MAX_ITEMS
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                and key not in self.cache_data:
            oldest_key = next(iter(self.cache_data))
            del self.cache_data[oldest_key]
            print("DISCARD: {}".format(oldest_key))

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
