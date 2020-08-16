from typing import List
import collections


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rowSets = [set() for _ in range(9)]  # each set represents element of a row
        colSets = [set() for _ in range(9)]
        subBoardSets = [[set() for _ in range(3)] for _ in range(3)]
        emptyBox = collections.deque()  # stores (row, col, 1) that dont have number in the beginning

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
                        emptyBox.appendleft((row, col))
                    else:
                        rowSets[row].add(int(a))
                        colSets[col].add(int(a))
                        subBoardSets[row // 3][col // 3].add(int(a))

        def add(row, col, val):
            emptyBox.popleft()
            rowSets[row].add(val)
            colSets[col].add(val)
            subBoardSets[row // 3][col // 3].add(val)
            board[row][col] = str(val)

        def remove(row, col, val):
            board[row][col] = '.'
            rowSets[row].remove(val)
            colSets[col].remove(val)
            subBoardSets[row // 3][col // 3].remove(val)
            emptyBox.appendleft((row, col))

        def dfs() -> bool:
            if not emptyBox: return True
            r, c = emptyBox.popleft()
            for v in range(10):
                if v not in rowSets[r] and v not in colSets[c] and v not in subBoardSets[r // 3][c // 3]:
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
