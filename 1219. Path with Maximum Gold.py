from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        """
        Idea:
            Try each path, return the maximum value
        """
        self.max_gold = 0
        self.current_gold = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                self.dfs(grid, r, c)

        return self.max_gold

    def dfs(self, grid: List[List[int]], row: int, col: int) -> None:
        """
        Idea:
            if the cell is in the grid and it has gold:
                collect it
                reach out to all neighbors
                when return to this cell:
                compare to the best path
                put back the gold
        """
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col]:
            collected = grid[row][col]
            self.current_gold += collected
            grid[row][col] = 0
            self.dfs(grid, row + 1, col)
            self.dfs(grid, row - 1, col)
            self.dfs(grid, row, col + 1)
            self.dfs(grid, row, col - 1)
            self.max_gold = max(self.max_gold, self.current_gold)
            self.current_gold -= collected
            grid[row][col] = collected
