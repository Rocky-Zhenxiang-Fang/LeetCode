class Solution:
    def numSquares(self, n: int) -> int:
        import math
        candidate = []
        for i in range(1, math.ceil(n ** 0.5)):
            candidate.append(i ** 2)
        dp = [i for i in range(n + 1)]
        for c in candidate:
            for i in range(1, len(dp)):
                if i >= c:
                    dp[i] = min(dp[i], dp[i  - c] + 1)
        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSquares(13))