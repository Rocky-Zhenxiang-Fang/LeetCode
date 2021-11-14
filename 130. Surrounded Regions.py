from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        Idea:
            Look around the edge and do DFS if find a "O", mark it as "#"
            Flip all remaining "O" to "X"
            Flip all "#" to "O"
        """
        for col in range(len(board[0])):
            if board[0][col] == "O":
                self._mark(board, 0, col, "O", "#")
            if board[len(board) - 1][col] == "O":
                self._mark(board, len(board) - 1, col, "O", "#")
        for row in range(len(board)):
            if board[row][0] == "O":
                self._mark(board, row, 0, "O", "#")
            if board[row][len(board[0]) - 1] == "O":
                self._mark(board, row, len(board[0]) - 1, "O", "#")
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O":
                    self._mark(board, row, col, "O", "X")
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "#":
                    self._mark(board, row, col, "#", "O")
            
        
        
    def _mark(self, board, row, col, target, result) -> None:
        stack = [(row, col)]
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while stack:
            r, c = stack.pop()
            board[r][c] = result
            for m in moves:
                new_r, new_c = r + m[0], c + m[1]
                if 0 <= new_r < len(board) and 0 <= new_c < len(board[0]) and board[new_r][new_c] == target:
                    stack.append((new_r, new_c))
            
    

if __name__ == "__main__":
    sol = Solution()
    arr = [["X","O","X"],["O","X","O"],["X","O","X"]]
    sol.solve(arr)
    print(arr)
    
    
    

        