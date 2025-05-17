#!/usr/bin/python3
""" LFU Cache Module """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU (Least Frequently Used) Caching System"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = {}       # {key: usage_count}
        self.access_order = []    # Tracks access order for LRU tie-breaking

    def put(self, key, item):
        """Add an item in the cache using LFU algorithm"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.access_order.remove(key)
            self.access_order.append(key)
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys = [
                k for k, freq in self.frequency.items() if freq == min_freq
            ]

            if len(lfu_keys) > 1:
                for k in self.access_order:
                    if k in lfu_keys:
                        discard_key = k
                        break
            else:
                discard_key = lfu_keys[0]

            del self.cache_data[discard_key]
            del self.frequency[discard_key]
            self.access_order.remove(discard_key)
            print(f"DISCARD: {discard_key}")

        self.cache_data[key] = item
        self.frequency[key] = 1
        self.access_order.append(key)

    def get(self, key):
        """Retrieve item from cache and update its usage frequency"""
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
