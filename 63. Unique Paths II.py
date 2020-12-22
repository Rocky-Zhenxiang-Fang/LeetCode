from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        For increasing efficiency, use obstacleGrid as dp
        """
        dp = [[0 for _ in range(len(obstacleGrid[0]) + 1)] for _ in range(len(obstacleGrid) + 1)]
        if obstacleGrid[0][0] != 1:
            dp[1][1] = 1     # starting point
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if obstacleGrid[row - 1][col - 1] != 1 and (row, col) != (1, 1):
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[-1][-1]


if __name__ == '__main__':
    obstacleGrid = [[1]]
    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))



