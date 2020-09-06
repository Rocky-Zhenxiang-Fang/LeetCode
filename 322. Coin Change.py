from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf") for _ in range(amount + 1)] for _ in range(len(coins) + 1)]
        for row in dp:
            row[0] = 0
        for row in range(1, len(dp)):
            curr = coins[row - 1]
            for col in range(1, len(dp[0])):
                if col >= curr:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - curr] + 1)
                else:
                    dp[row][col] = dp[row - 1][col]

        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1

if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))