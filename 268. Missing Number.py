from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        est_sum = len(nums) * (len(nums) + 1) // 2
        return est_sum - sum(nums)
