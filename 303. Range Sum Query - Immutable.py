from typing import List


class NumArray:
    """
    Idea:
        Just like finding the sum of each subarray
    """

    def __init__(self, nums: List[int]):
        self.sub_sum = [0]
        sums = 0
        for n in nums:
            sums += n
            self.sub_sum.append(sums)

    def sumRange(self, i: int, j: int) -> int:
        return self.sub_sum[j] - self.sub_sum[i - 1]

