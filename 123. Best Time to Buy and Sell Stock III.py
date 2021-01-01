from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        From: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/149383/Easy-DP-solution-using-state-machine-O(n)-time-complexity-O(1)-space-complexity
        Idea: in each time, the buyer might be at either one state:
            0. no transaction, not holding stock
            1. no transaction, holding stock
            2. one transaction, not holding stock
            3. one transaction, holding stock
            4. two transactions
            In each state, the best strategy is to maximum the local profit, in state 0, 2, we can only spend money, and
            in 1, 3, we can only sell stock.
            This approach is better then the greedy approach because it preserves the possibility of two transaction might
            be one transaction
        """
        if not prices:
            return 0
        s1, s2, s3, s4 = -prices[0], -float("inf"), -float("inf"), -float("inf")
        for i in range(len(prices)):
            s1 = max(s1, -prices[i])    # either do nothing or buy at time i
            s2 = max(s2, s1 + prices[i])    # do nothing or earn the price difference between s1 and price[i]
            s3 = max(s3, s2 - prices[i])
            s4 = max(s4, s3 + prices[i])
        return max(0, s4)


if __name__ == '__main__':
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    sol = Solution()
    print(sol.maxProfit(prices))
