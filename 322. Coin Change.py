from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[float("inf") for _ in range(amount)] for _ in range(len(coins))]
        for i in range(len(dp[0])):
            if (i + 1) % coins[0] == 0:
                dp[0][i] = (i + 1) // coins[0]
        for row in range(1, len(dp)):
            current = coins[row]
            for col in range(len(dp[0])):
                if col + 1 >= current:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col + 1 - current] + 1)
        return -1 if dp[-1][-1] == float("inf") else dp[-1][-1]


if __name__ == '__main__':
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.coinChange(coins, amount))