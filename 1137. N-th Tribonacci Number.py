class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            dp = [0, 1, 1]
            while 2 < n:
                dp = dp[1:] + [sum(dp)]
                n -= 1

        return dp[-1]
