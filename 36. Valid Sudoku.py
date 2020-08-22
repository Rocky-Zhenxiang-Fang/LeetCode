from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSets = [set() for _ in range(9)]
        colSets = [set() for _ in range(9)]
        subSets = [[set() for _ in range(3)] for _ in range(3)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val in rowSets[row] or val in colSets[col] or val in subSets[row // 3][col // 3]:
                    return False
                else:
                    rowSets[row].add(val)
                    colSets[col].add(val)
                    subSets[row // 3][col // 3].add(val)
        return True


if __name__ == '__main__':
    arr = [[".", "8", "7", "6", "5", "4", "3", "2", "1"],
           ["2", ".", ".", ".", ".", ".", ".", ".", "."],
           ["3", ".", ".", ".", ".", ".", ".", ".", "."],
           ["4", ".", ".", ".", ".", ".", ".", ".", "."],
           ["5", ".", ".", ".", ".", ".", ".", ".", "."],
           ["6", ".", ".", ".", ".", ".", ".", ".", "."],
           ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           ["8", ".", ".", ".", ".", ".", ".", ".", "."],
           ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    sol = Solution()
    print(sol.isValidSudoku(arr))
