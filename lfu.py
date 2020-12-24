from collections import Counter


class LFUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.frequency_dict = Counter()  # for counting frequency of keys

    def get(self, key):

        if key in self.cache:
            # increase the frequency by one for accessed key
            self.frequency_dict[key] += 1
            return self.cache.get(key)
        return -1

    def set(self, key, value):

        if not (key in self.cache) and len(self.cache) == self.capacity:
            # find least recently used key and remove it
            lfu_key = self.frequency_dict.most_common()[-1][0]
            del self.cache[lfu_key]
            del self.frequency_dict[lfu_key]
        self.cache[key] = value
        self.frequency_dict[key] += 1
