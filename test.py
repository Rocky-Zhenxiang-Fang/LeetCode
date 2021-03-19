from typing import List, Tuple

from DS import TreeNode
import collections


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.trie
        for ch in word:
            if ch not in ptr:
                ptr[ch] = {}
            ptr = ptr[ch]
        ptr["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.trie
        for ch in word:
            if ch not in ptr:
                return False
            ptr = ptr[ch]
        return "#" in ptr

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.trie
        for ch in prefix:
            if ch not in ptr:
                return False
            ptr = ptr[ch]
        return True


if __name__ == '__main__':
    pass