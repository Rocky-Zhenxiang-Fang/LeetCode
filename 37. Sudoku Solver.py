from typing import List
from collections import defaultdict, deque
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows, cols, sqas, pits = defaultdict(set), defaultdict(set), defaultdict(set), deque([])

        def init() -> None:
            """
            search all box in the board,
            if it is ".", add the index into emptyBox,
            if it has a value, add the value in to the corresponding
            rowSets[], colSets[], emptyBoxSets[]
            """
            for row in range(len(board)):
                for col in range(len(board[0])):
                    a = board[row][col]
                    if a == '.':
                        pits.appendleft((row, col))
                    else:
                        rows[row].add(int(a))
                        cols[col].add(int(a))
                        sqas[(row // 3, col // 3)].add(int(a))

        def add(row, col, val):
            rows[row].add(val)
            cols[col].add(val)
            sqas[(row // 3, col // 3)].add(val)
            board[row][col] = str(val)
            pits.popleft()

        def remove(row, col, val):
            board[row][col] = '.'
            rows[row].discard(val)
            cols[col].discard(val)
            sqas[(row // 3, col // 3)].discard(val)
            pits.appendleft((row, col))

        def dfs() -> bool:
            if not pits: return True
            r, c = pits[0]
            for v in range(1, 10):
                if v not in rows[r] and v not in cols[c] and v not in sqas[(r // 3, c // 3)]:
                    add(r, c, v)
                    if dfs():
                        return True
                    remove(r, c, v)
            return False

        init()
        dfs()


if __name__ == '__main__':
    sol = Solution()
    inputBoard = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    sol.solveSudoku(inputBoard)
    print(inputBoard)
