from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        如果在區域最小值，買進
        如果在區域最大值，賣出
        """
        if len(prices) == 0:
            return 0
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))

