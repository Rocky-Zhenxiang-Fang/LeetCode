from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0] and self.find(board, word, 0, r, c):
                    return True
        return False
        
    def find(self, board: List[List[str]], word: str, ptr: int, row: int, col: int) -> bool:
        if ptr == len(word):
            return True
        
        if 0 <= row < len(board) and 0 <= col < len(board[0]):
            if board[row][col] == word[ptr]:
                board[row][col] = "#"
                if self.find(board, word, ptr + 1, row + 1, col) or \
                    self.find(board, word, ptr + 1, row, col + 1) or \
                    self.find(board, word, ptr + 1, row - 1, col) or \
                    self.find(board, word, ptr + 1, row, col - 1):
                    return True
                board[row][col] = word[ptr]

        return False


if __name__ == '__main__':
    sol = Solution()
    b = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    s = "ABCESEEEFS"
    print(sol.exist(b, s))


