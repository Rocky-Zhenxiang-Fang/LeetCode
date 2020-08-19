from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        res: List[List[int]] = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res[0][0] = grid[0][0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if row == 0 and col == 0:
                    continue
                elif row == 0:
                    res[row][col] = res[row][col - 1] + grid[row][col]
                elif col == 0:
                    res[row][col] = res[row - 1][col] + grid[row][col]
                else:
                    res[row][col] = min(res[row][col - 1], res[row - 1][col]) + grid[row][col]
        return res[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    g = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    print(sol.minPathSum(g))