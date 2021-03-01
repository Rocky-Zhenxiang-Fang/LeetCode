from typing import List


class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        """
        Idea:
            DP, each cell stores length from (left, left_up, up, right_up), at each node, see the value if its neighbor node
            and add 1 to it
        """
        if not M:
            return 0
        res = 0
        dp = [[[0, 0, 0, 0] for _ in range(len(M[0]))] for _ in range(len(M))]
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 1:
                    dp[row][col] = [1, 1, 1, 1]
                    if col != 0:
                        dp[row][col][0] += dp[row][col - 1][0]
                    if col != 0 and row != 0:
                        dp[row][col][1] += dp[row - 1][col - 1][1]
                    if row != 0:
                        dp[row][col][2] += dp[row - 1][col][2]
                    if row != 0 and col != len(M[0]) - 1:
                        dp[row][col][3] += dp[row - 1][col + 1][3]
                    res = max(res, max(dp[row][col]))
        return res


if __name__ == '__main__':
    sol = Solution()
    M = [[0,0],[1,1]]
    print(sol.longestLine(M))
