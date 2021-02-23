from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        for i in range(len(nums) + 1):
            prev = nums[i - 1] if i != 0 else lower - 1
            curr = nums[i] if i < len(nums) else upper + 1
            if curr - 1 > prev:
                if curr - 1 == prev + 1:
                    res.append(str(prev + 1))
                else:
                    res.append(str(prev + 1) + "->" + str(curr - 1))

        return res
