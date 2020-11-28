from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            negative_index = abs(nums[i]) - 1
            nums[negative_index] = -abs(nums[negative_index])
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res