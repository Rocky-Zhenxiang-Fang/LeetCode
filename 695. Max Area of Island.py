from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.explore(i, j, grid, 0))
        return max_area

    def explore(self, row, col, grid, area) -> int:
        area += 1
        grid[row][col] = 0
        if row - 1 >= 0 and grid[row - 1][col] == 1:
            area = self.explore(row - 1, col, grid, area)
        if row + 1 < len(grid) and grid[row + 1][col] == 1:
            area = self.explore(row + 1, col, grid, area)
        if col - 1 >= 0 and grid[row][col - 1] == 1:
            area = self.explore(row, col - 1, grid, area)
        if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
            area = self.explore(row, col + 1, grid, area)
        return area


if __name__ == '__main__':
    test_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    sol = Solution()
    print(sol.maxAreaOfIsland(test_grid))
