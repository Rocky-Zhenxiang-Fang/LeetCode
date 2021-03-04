from typing import List, Dict, Set


class Trie:
    def __init__(self):
        self.check = {}

    def insert(self, word: str):
        ite = self.check
        for ch in word:
            if ch not in ite:
                ite[ch] = {}
            ite = ite[ch]
        ite["#"] = "#"


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Idea:
            Naive: search each words one by one as if is a Word search problem. Cost a lot of time
            Advance: Use a trie to prevent dealing the same prefix multiple time
        Alg:
            Construct a trie
            for each cell in board:
                if it is in the first layer of trie:
                    do dfs to find if we can find a word by moving in four direction
        """
        trie = Trie()
        res = []
        for w in words:
            trie.insert(w)
        for r in range(len(board)):
            for c in range(len(board[0])):
                self.dfs(board, trie.check, r, c, res, [])
        return res

    def dfs(self, board: List[List[str]], trie: Dict, row: int, col: int, res: List[str], prefix: [], ):
        if board[row][col] in trie:
            ch = board[row][col]
            board[row][col] = "-"       # this prevents using a visited set
            prefix.append(ch)
            if "#" in trie[ch]:
                res.append("".join(prefix))
                trie[ch].pop("#")   # this prevents duplicates
            for m in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                nr, nc = row + m[0], col + m[1]
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]):
                    self.dfs(board, trie[ch], nr, nc, res, prefix)
            prefix.pop()
            board[row][col] = ch


if __name__ == '__main__':
    sol = Solution()
    board = [["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]]
    words = ["oa", "oaa"]
    print(sol.findWords(board, words))
