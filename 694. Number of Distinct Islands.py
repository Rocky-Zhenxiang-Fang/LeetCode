from typing import List, Set, Tuple


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        distinct_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    shape = set()
                    self._explore(i, j, i, j, grid, shape)
                    distinct_islands.add(frozenset(shape))
        return len(distinct_islands)

    def _explore(self, o_r, o_c, row, col, grid, shape):
        """
        get the local coordinate of an island and store it in shape
        """
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            shape.add((row - o_r, col - o_c))
            grid[row][col] = 0
            self._explore(o_r, o_c, row + 1, col, grid, shape)
            self._explore(o_r, o_c, row - 1, col, grid, shape)
            self._explore(o_r, o_c, row, col + 1, grid, shape)
            self._explore(o_r, o_c, row, col - 1, grid, shape)
        return


if __name__ == '__main__':
    g_1 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    g_2 = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    sol = Solution()
    print(sol.numDistinctIslands(g_1))
    print(sol.numDistinctIslands(g_2))
