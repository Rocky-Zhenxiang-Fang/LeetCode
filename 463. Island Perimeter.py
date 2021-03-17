from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        Idea:
            Do DFS, if a side is near to ocean, perimeter += 1
        """
        self.perimter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    self._DFS(grid, row, col)
                    break

        return self.perimter

    def _DFS(self, grid, row, col):
        grid[row][col] = -1
        move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for d_r, d_c in move:
            r = row + d_r
            c = col + d_c
            if 0 > r or r >= len(grid) or 0 > c or c >= len(grid[0]) or grid[r][c] == 0:
                self.perimter += 1
            elif grid[r][c] == 1:
                self._DFS(grid, r, c)


if __name__ == '__main__':
    sol = Solution()
    g = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    print(sol.islandPerimeter(g))
