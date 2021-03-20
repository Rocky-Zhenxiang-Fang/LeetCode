from typing import List, Tuple

from DS import TreeNode
import collections


class Solution:
    class Trie:
        def __init__(self):
            self.trie = {}

        def insert(self, word: str):
            ptr = self.trie
            for ch in word:
                if ch not in ptr:
                    ptr[ch] = {}
                ptr = ptr[ch]
            ptr["#"] = "#"

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = self.Trie()
        for w in words:
            trie.insert(w)
        res = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in trie.trie:
                    self._dfs(board, trie.trie, row, col, [], res)

        return res

    def _dfs(self, board, trie, row, col, current, res):
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        if board[row][col] in trie:
            hold = board[row][col]
            board[row][col] = "@"
            trie = trie[hold]
            current.append(hold)
            if "#" in trie:
                res.append("".join(current))
                trie.pop("#")
            for m in moves:
                r, c = row + m[0], col + m[1]
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != "@":
                    self._dfs(board, trie, r, c, current, res)
            current.pop()
            board[row][col] = hold


if __name__ == '__main__':
    pass
