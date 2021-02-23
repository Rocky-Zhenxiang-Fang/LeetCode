from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = [int(i) for i in matrix[0]]
        max_side = max(dp)
        for row in range(1, len(matrix)):
            new_dp = [0] * len(matrix[0])
            for col in range(len(matrix[0])):
                if col == 0:
                    new_dp[0] = int(matrix[row][0])
                else:
                    if int(matrix[row][col]) == 1:
                        new_dp[col] = min(new_dp[col - 1], dp[col], dp[col - 1]) + 1
                max_side = max(max_side, new_dp[col])
            dp = new_dp

        return max_side ** 2


if __name__ == '__main__':
    matrix = [["0", "1"], ["1", "0"]]
    sol = Solution()
    print(sol.maximalSquare(matrix))
