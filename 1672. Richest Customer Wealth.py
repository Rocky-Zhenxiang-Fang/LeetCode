from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = 0
        for peo in accounts:
            res = max(res, sum(peo))
        return res
