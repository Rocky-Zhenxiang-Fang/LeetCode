from typing import List


class Solution(object):
    def maxProfit(self, prices, fee):
        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        return cash

if __name__ == '__main__':
    sol = Solution()
    p = [1, 3, 7, 5, 10, 3]
    f = 3
    print(sol.maxProfit(p, f))
