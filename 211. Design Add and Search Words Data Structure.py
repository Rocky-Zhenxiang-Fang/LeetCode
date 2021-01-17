class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = {}

    def addWord(self, word: str) -> None:
        ite = self.head
        for c in word:
            if c not in ite:
                ite[c] = {}
            ite = ite[c]
        ite["#"] = {}

    def search(self, word: str) -> bool:
        """
        How to deal with ".":
            Can do a dfs or bfs on all key in that dict
        """
        return self._dfs(self.head, word, 0)

    def _dfs(self, ite, word, index) -> bool:
        if index == len(word):
            return "#" in ite
        if word[index] != ".":
            if word[index] not in ite:
                return False
            else:
                return self._dfs(ite[word[index]], word, index + 1)
        else:
            for key in ite:
                if self._dfs(ite[key], word, index + 1):
                    return True
            return False


if __name__ == '__main__':
    word = WordDictionary()
    print(word.addWord("bad"))
    print(word.addWord("dad"))
    print(word.addWord("mad"))
    print(word.addWord("pad"))
    print(word.search("bad"))
    print(word.search(".ad"))
    print(word.search("b.."))
    print(word.search("aaa"))
