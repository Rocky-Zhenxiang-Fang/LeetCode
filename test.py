# This file is used to review done questions

# Definition for a binary tree node.
from typing import List, Set

import DS


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Idea: When adding a new number, first check the entire array nums[:i]
            Then, see if this array can be decided into two parts, nums[:j] + nums[j + 1:k]
            Where sum(nums[:j]) + sum(nums[j + 1 : k]) == k
            Since nums[:J] will be visited earlier, we can store its sum in a map, then treat it
            as a Two Sum problem
            Note:
                Can use running sum instead of sum() to get a better runtime
        """
        seen = {}
        running = 0
        res = 0
        for i in range(len(nums)):
            running += nums[i]
            if running == k:
                res += 1
            if running - k in seen:
                res += seen[running - k]
            seen[running] = seen.get(running, 0) + 1

        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 3
    sol = Solution()
    print(sol.subarraySum(nums, k))
