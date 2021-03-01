from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        """
        Idea:
            Two pointers, keep increase right pointer until the subarray is not increasing, compare the length,
            Move both right and left to the right pointer
        """
        if not nums:
            return 0
        left, right = 0, 0
        res = 1
        while right < len(nums):
            while right + 1 < len(nums) and nums[right + 1] > nums[right]:
                right += 1
            res = max(res, right - left + 1)
            right += 1
            left = right
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [1,3,5,4,7]
    print(sol.findLengthOfLCIS(arr))
