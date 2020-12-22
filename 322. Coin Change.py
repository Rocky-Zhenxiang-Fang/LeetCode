from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0
        for i in range(1, len(dp)):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[-1] == float("inf") else dp[-1]


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))