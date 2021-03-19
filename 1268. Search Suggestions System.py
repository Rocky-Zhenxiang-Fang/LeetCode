from typing import List


class Solution:
    class Trie:
        def __init__(self):
            self.children = [None] * 27

        def insert(self, word: str):
            ptr = self.children
            for ch in word:
                if not ptr[ord(ch) - ord("a")]:
                    ptr[ord(ch) - ord("a")] = [None] * 27
                ptr = ptr[ord(ch) - ord("a")]
            ptr[-1] = "#"

        def find_three_prefix(self, searchWord: str, end_index: int) -> List[str]:
            ptr = self.children
            res = []
            for i in range(end_index + 1):
                ch = searchWord[i]
                if not ptr[ord(ch) - ord("a")]:
                    return res
                ptr = ptr[ord(ch) - ord("a")]
            stack = [(ptr, list(searchWord[:end_index + 1]))]
            while stack:
                curr, word = stack.pop()
                if curr[-1]:
                    res.append("".join(word))
                    if len(res) == 3:
                        break
                for i in range(25, -1, -1):
                    if curr[i]:
                        stack.append((curr[i], word + [chr(i + ord("a"))]))
            return res

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        trie = self.Trie()
        for p in products:
            trie.insert(p)
        res = []
        for i in range(len(searchWord)):
            s = trie.find_three_prefix(searchWord, i)
            res.append(s)
        return res


if __name__ == '__main__':
    sol = Solution()
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(sol.suggestedProducts(products, searchWord))
