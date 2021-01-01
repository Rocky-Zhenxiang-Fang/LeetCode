from typing import List
import random


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        from collections import Counter
        counter = Counter(nums)
        res = []
        for n in counter:
            if counter[n] > len(nums) // 3:
                res.append(n)
        return res

    def majorityElement_2(self, nums: List[int]) -> List[int]:
        m1, m2, ct1, ct2 = -1, -1, 0, 0
        res = []
        for n in nums:
            if n == m1:
                ct1 += 1
            elif n == m2:
                ct2 += 1
            elif ct1 == 0:
                m1 = n
                ct1 = 1
            elif ct2 == 0:
                m2 = n
                ct2 = 1
            else:
                ct1 -= 1
                ct2 -= 1

        m1_ctr = 0
        m2_ctr = 0
        for n in nums:
            if n == m1:
                m1_ctr += 1
            elif n == m2:
                m2_ctr += 1
        if m1_ctr > len(nums) // 3:
            res.append(m1)
        if m2_ctr > len(nums) // 3:
            res.append(m2)
        return res


if __name__ == '__main__':
    sol = Solution()
    nums1 = [3, 2, 3]
    nums2 = [1]
    nums3 = [1, 2]
    print(sol.majorityElement(nums1))
    print(sol.majorityElement(nums2))
    print(sol.majorityElement(nums3))
    nums4 = [random.randint(0, 2) for _ in range(10)]
    print(nums4)
    print(sol.majorityElement(nums4))
    print(sol.majorityElement_2(nums4))
