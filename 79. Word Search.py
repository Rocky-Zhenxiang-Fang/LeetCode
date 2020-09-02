from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Iterate though the entire board, if a block matches the first ch in word,
        use dfs to find if the board contains the entire word
        If not, return False
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word, 0):
                        return True
        return False

    def dfs(self, board, row, col, word, index):
        # Base case, if index == len(word), this means that all ch in words has been found, so return True
        if index == len(word):
            return True
        # Checks the boundary, if exceeds the board, this cannot be the right path, return False
        if row == -1 or row == len(board) or col == -1 or col == len(board[0]):
            return False
        # Check if this block matches, if not, return False
        if board[row][col] != word[index]:
            return False
        # To prevent using a block twice, if a block is used, then it is set to a ch that will never be assigned
        hold = board[row][col]  # used to store information to be fill back
        board[row][col] = "1"
        # Since this block matches, check if any of its neighbor has the next character. If any of its neighbor finished
        # the word, return True
        if (self.dfs(board, row + 1, col, word, index + 1) or
                self.dfs(board, row - 1, col, word, index + 1) or
                self.dfs(board, row, col + 1, word, index + 1) or
                self.dfs(board, row, col - 1, word, index + 1)):
            return True
        else:  # Since none of its neighbor has the next character, we fill back the board, and return False
            board[row][col] = hold
            return False


