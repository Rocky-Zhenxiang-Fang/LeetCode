from typing import List
import collections


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_counter = collections.Counter(nums1)
        nums2_counter = collections.Counter(nums2)
        res = []
        if len(nums1_counter) > len(nums2_counter):
            nums2_counter, nums1_counter = nums1_counter, nums2_counter
        for k in nums1_counter:
            if k in nums2_counter:
                res += [k] * min(nums1_counter[k], nums2_counter[k])
        return res


if __name__ == '__main__':
    sol = Solution()
    a1 = [1, 2, 2, 1]
    a2 = [2, 2]
    print(sol.intersect(a1, a2))
