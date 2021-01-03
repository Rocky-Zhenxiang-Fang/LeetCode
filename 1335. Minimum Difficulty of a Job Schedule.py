class Solution:
    def minDifficulty(self, A, d):
        n, inf = len(A), float('inf')
        if n < d: return -1
        dp = [inf] * n + [0]
        for d in range(1, d + 1):
            for i in range(n - d + 1):
                maxd, dp[i] = 0, inf
                for j in range(i, n - d + 1):
                    maxd = max(maxd, A[j])
                    dp[i] = min(dp[i], maxd + dp[j + 1])
        return dp[0]