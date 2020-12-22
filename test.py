# This file is used to review done questions

# Definition for a binary tree node.
from typing import List

import DS


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[-1] == float("inf") else dp[-1]


if __name__ == '__main__':
    nums = [1, 2, 5]
    target = 11
    sol = Solution()
    print(sol.coinChange(nums, target))
