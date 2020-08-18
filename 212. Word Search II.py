from typing import List

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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(currBoard, tree: dict, i, j, result, path='') -> None:
            """
            :param currBoard: board
            :param tree: dict of trie at current level
            :param i: row of the board
            :param j: column of the board
            :param result: res
            :param path: added word
            """
            if currBoard[i][j] not in tree:
                return
            else:
                tree: dict = tree[currBoard[i][j]]
                c = currBoard[i][j]
                path += c
                currBoard[i][j] = '*'
                if "#" in tree:
                    result.append(path)
                    tree.pop("#")
                if i != 0:
                    dfs(currBoard, tree, i - 1, j, result, path)
                if i != len(currBoard) - 1:
                    dfs(currBoard, tree, i + 1, j, result, path)
                if j != 0:
                    dfs(currBoard, tree, i, j - 1, result, path)
                if j != len(currBoard[0]) - 1:
                    dfs(currBoard, tree, i, j + 1, result, path)
                currBoard[i][j] = c

        res, trie = [], Trie()
        t = trie.dict
        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, t, i, j, res,)

        return res


if __name__ == '__main__':
    sol = Solution()
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print(sol.findWords(board, words))