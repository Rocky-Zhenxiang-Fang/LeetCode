from typing import Optional, List


class ListNode:
    def __init__(self, key: int = -1000, val: int = -1000):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets: List[Optional[ListNode]] = [ListNode()] * 2069

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        bu = self._hash(key)
        prev = self.buckets[bu]
        ite = prev.next
        while ite and ite.key != key:
            prev = ite
            ite = ite.next
        if not ite:
            prev.next = ListNode(key, value)
        else:
            ite.val = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bu = self._hash(key)
        ite = self.buckets[bu]
        while ite:
            if ite.key == key:
                return ite.val
            else:
                ite = ite.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bu = self._hash(key)
        prev = self.buckets[bu]
        ite = prev.next
        while ite and ite.key != key:
            prev = ite
            ite = ite.next

        if ite:
            prev.next = ite.next

    def _hash(self, key: int) -> int:
        return key % len(self.buckets)