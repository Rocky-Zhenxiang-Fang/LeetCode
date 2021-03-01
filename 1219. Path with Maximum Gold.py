from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Idea:
            Try each path using DFS, return the maximum value
        """
        self.res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.dfs(grid, r, c, 0)
        return self.res

    def dfs(self, grid, row: int, col: int, path_sum):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] != 0:
            collected = grid[row][col]
            grid[row][col] = 0
            self.res = max(self.res, path_sum + collected)
            moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for m in moves:
                self.dfs(grid, row + m[0], col + m[1], path_sum + collected)
            grid[row][col] = collected


if __name__ == '__main__':
    sol = Solution()
    grid = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
    print(sol.getMaximumGold(grid))


