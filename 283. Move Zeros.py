from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextNonZero = 0
        itr = 0
        while itr < len(nums):
            if nums[itr] != 0:
                nums[nextNonZero], nums[itr] = nums[itr], nums[nextNonZero]
                nextNonZero += 1
            itr += 1