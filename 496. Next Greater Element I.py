from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Idea:
            Using monostack to prevent multiple lookup,
            As long as finding a latter element bigger then previous element, we know that the next bigger element of
            previous element is this current element
        """
        stack = []
        lookup = {}
        res = []
        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                lookup[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        for n in nums1:
            if n in lookup:
                res.append(lookup[n])
            else:
                res.append(-1)

        return res


if __name__ == '__main__':
    sol = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(sol.nextGreaterElement(nums1, nums2))
