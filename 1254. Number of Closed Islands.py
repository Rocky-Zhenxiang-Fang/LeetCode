from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0 and self._dfs(grid, r, c):
                    res += 1
        return res
                    
    def _dfs(self, grid, row, col) -> bool:
        if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
            return False
        if grid[row][col] == 1:
            return True
        grid[row][col] = 1
        res = True
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for m in moves:
            res &= self._dfs(grid, row + m[0], col + m[1])
        return res


if __name__ == '__main__':
    sol = Solution()
    grid = [[1,1,1,1,1,1,1,0],
            [1,0,0,0,0,1,1,0],
            [1,0,1,0,1,1,1,0],
            [1,0,0,0,0,1,0,1],
            [1,1,1,1,1,1,1,0]]
    print(sol.closedIsland(grid))