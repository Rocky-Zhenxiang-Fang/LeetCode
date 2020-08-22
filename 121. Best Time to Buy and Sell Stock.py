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
        if len(prices) == 0:
            return 0
        buyPrice = prices[0]
        maxPro = 0
        for i in range(len(prices) - 1):
            buyPrice = min(buyPrice, prices[i])
            maxPro = max(maxPro, prices[i + 1] - buyPrice)
        return maxPro


if __name__ == '__main__':
    sol = Solution()
    pri = [7,6,4,3,1]
    print(sol.maxProfit(pri))
