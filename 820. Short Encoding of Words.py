from typing import List, Dict


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        """
        Idea:
            do a suffix trie, if a node is end and has no neighbor, then the word is the longest, put it into the result
        """
        trie = {}
        word_check = {}  # stores(word: trie_node)
        res = 0
        words = set(words)
        for w in words:
            word_check[w] = self._add_suffix(trie, w)
        for w, node in word_check.items():
            if len(node) == 1:
                res += len(w) + 1

        return res

    def _add_suffix(self, trie: Dict, word: str) -> Dict:
        for i in range(len(word) - 1, -1, -1):
            if word[i] not in trie:
                trie[word[i]] = {}
            trie = trie[word[i]]
        trie["#"] = "#"
        return trie


if __name__ == '__main__':
    sol = Solution()
    ws = ["time", "me", "bell"]
    print(sol.minimumLengthEncoding(ws))
