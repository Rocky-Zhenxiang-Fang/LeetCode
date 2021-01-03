from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_len = 0
        dp = [[0 for _ in range(len(matrix[0]) + 1)] for _ in range(len(matrix) + 1)]
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                if matrix[row - 1][col - 1] == "1":
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col - 1]) + 1
                    max_len = max(max_len, dp[row][col])
        return max_len ** 2


if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    sol = Solution()
    print(sol.maximalSquare(matrix))
