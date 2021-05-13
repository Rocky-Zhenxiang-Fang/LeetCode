from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res = max(res, self._dfs(grid, r, c, moves))
        return res

    def _dfs(self, grid: List[List[int]], row: int, col: int, moves) -> int:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0
        else:
            res = 1
            grid[row][col] = 0
            for m in moves:
                res += self._dfs(grid, row + m[0], col + m[1], moves)
            return res


if __name__ == '__main__':
    test_grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    sol = Solution()
    print(sol.maxAreaOfIsland(test_grid))
