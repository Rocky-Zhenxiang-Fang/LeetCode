from typing import List, Set, Tuple


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        """
        Idea: similar to number of islands, but this time, we need to find a way to record "distinct" island
            To do this, we can use local coordinate, assume that the first point we meet is (0, 0), then record
            other local coordinates that is "1"
        """
        distinct_shapes = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    shape = set()
                    self.explore(grid, row, col, row, col, shape)
                    distinct_shapes.add(frozenset(shape))
        return len(distinct_shapes)

    def explore(self, grid: List[List[int]], row: int, col: int, row_o: int, col_o: int, shape: Set[Tuple[int, int]]):
        if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1:
            grid[row][col] = 0
            shape.add((row - row_o, col - col_o))
            self.explore(grid, row + 1, col, row_o, col_o, shape)
            self.explore(grid, row - 1, col, row_o, col_o, shape)
            self.explore(grid, row, col + 1, row_o, col_o, shape)
            self.explore(grid, row, col - 1, row_o, col_o, shape)


if __name__ == '__main__':
    g_1 = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    g_2 = [[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]]
    sol = Solution()
    print(sol.numDistinctIslands(g_1))
    print(sol.numDistinctIslands(g_2))
