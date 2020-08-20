from typing import List


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        """
        Clear explanation: https://www.youtube.com/watch?v=duCx_62nMOA
        """
        dp = [[0 for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    A = [1, 3, 7, 1, 7, 5]
    B = [1, 9, 2, 5, 1]
    print(sol.maxUncrossedLines(A, B))
