from typing import List


class Solution:
    def maxProfitSlow(self, prices: List[int]) -> int:
        """
        Time Limit Exceeded: O(n^2)
        :param prices:
        :return:
        """
        maxPro = 0
        for i in range(len(prices) - 1):
            for j in range(i, len(prices)):
                profit = prices[j] - prices[i]
                maxPro = max(profit, maxPro)
        return maxPro

    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float("inf")
        max_profit = 0
        if not prices:
            return 0
        for p in prices:
            max_profit = max(max_profit, p - lowest_price)
            lowest_price = min(lowest_price, p)
        return max_profit

if __name__ == '__main__':
    sol = Solution()
    pri = [7,6,4,3,1]
    print(sol.maxProfit(pri))
