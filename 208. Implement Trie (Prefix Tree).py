class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ite = self.dict
        for c in word:
            if c not in ite:
                ite[c] = {}
            ite = ite[c]
        ite["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ite = self.dict
        for c in word:
            if c not in ite:
                return False
            ite = ite[c]

        return "#" in ite

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ite = self.dict
        for c in prefix:
            if c not in ite:
                return False
            ite = ite[c]
        return True


if __name__ == '__main__':
    obj = Trie()

    obj.insert("apple")
    print(obj.search("apple"))  # returns true
    print(obj.search("app"))  # returns false
    print(obj.startsWith("app"))  # returns true
    obj.insert("app")
    print(obj.search("app"))  # returns true
