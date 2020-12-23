from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/discuss/158940/Beat-100%3A-Very-Simple-(Python)-Very-Detailed-Explanation
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


if __name__ == '__main__':
    test_nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    print(sol.findMin(test_nums))
