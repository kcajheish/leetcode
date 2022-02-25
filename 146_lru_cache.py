"""
cache has capacity.
get/put time complexity: O(1)
if cache capacity is full, update removes the least recently used items first.

note: to search key in dequeue, time-complexity is O(capacity).
"""

from collections import deque

class LRUCacheV1:

    def __init__(self, capacity: int):
        self.deque = deque([])
        self.dic = dict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        self.deque.remove(key)
        self.deque.append(key)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.deque.remove(key)
        elif len(self.deque) == self.capacity:
            rm_key = self.deque.popleft()
            self.dic.pop(rm_key, None)
        self.deque.append(key)
        self.dic[key] = value

