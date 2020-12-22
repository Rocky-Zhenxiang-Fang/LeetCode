# This file is used to review done questions

# Definition for a binary tree node.
from typing import List

import DS


class Solution:
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
    nums = [7,6,4,3,1]
    sol = Solution()
    print(sol.maxProfit(nums))
