from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Idea:
            Similar to Find Minimum in Rotated Sorted Array
            If a slice of nums has the property: nums[left] < nums[right], this means that this part will be a straight line
            and will not contain our answer. Since nums[left] could still be the answer, we update right = left
            Else if nums[left] > nums[right], we know that this half will contain a dip, which is the answer. Since nums[left] already
            bigger then a number, we update left = mid + 1
            Else:   # nums[left] == nums[right], we are not sure what will happen, reduce the scope by one. We update right to right - 1
            since it is the one we used to compare, we will not miss it.
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right -= 1

        return nums[left]
