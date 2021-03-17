from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index_value = {}
        for i in range(len(nums)):
            if nums[i] != 0:
                self.index_value[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dict1 = self.index_value
        dict2 = vec.index_value
        res = 0
        if len(dict1) > len(dict2):
            dict1, dict2 = dict2, dict1     # always make sure that dict1 has the fewer elements
        for k, v, in dict1.items():
            if k in dict2:
                res += v * dict2[k]
        return res
