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
        ite = self.trie
        for ch in word:
            if ch not in ite:
                ite[ch] = {}
            ite = ite[ch]
        ite["#"] = "#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ite = self.trie
        for ch in word:
            if ch not in ite:
                return False
            else:
                ite = ite[ch]
        return "#" in ite

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ite = self.trie
        for ch in prefix:
            if ch not in ite:
                return False
            else:
                ite = ite[ch]
        return True


if __name__ == '__main__':
    obj = Trie()

    obj.insert("apple")
    print(obj.search("apple"))  # returns true
    print(obj.search("app"))  # returns false
    print(obj.startsWith("app"))  # returns true
    obj.insert("app")
    print(obj.search("app"))  # returns true
