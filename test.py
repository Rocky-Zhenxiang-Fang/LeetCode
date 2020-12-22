# This file is used to review done questions

# Definition for a binary tree node.
from typing import List

import DS


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            max_value = 1   # itself
            for j in range(i):
                if nums[i] > nums[j]:
                    max_value = max(max_value, dp[j] + 1)
            dp[i] = max_value
        return max(dp)

if __name__ == '__main__':
    nums = [0,1,0,3,2,3]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
