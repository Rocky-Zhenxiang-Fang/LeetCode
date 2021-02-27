from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        """
        Idea:
            Dp, each number in dp is the biggest length of square sub matrix the uses it as lower right corner
        """
        dp = [matrix[0][i] for i in range(len(matrix[0]))]
        res = sum(dp)
        for row in range(1, len(matrix)):
            new_dp = [matrix[row][0]]
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 1:
                    new_dp.append(min(dp[col - 1], new_dp[col - 1], dp[col]) + 1)
                else:
                    new_dp.append(0)
            res += sum(new_dp)
            dp = new_dp
        return res


if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]

    sol = Solution()
    print(sol.countSquares(matrix))

