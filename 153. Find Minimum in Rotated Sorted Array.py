from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Idea:
            Kinda sorted: Binary searched
            By drawing some example, we can see that if left > right, this means that there is a drop, where the answer is
            Thus, In each iteration, we want to make sure that the two end satisfied the condition
        """
        left, right = 0, len(nums) - 1
        if nums[right] > nums[left]:
            return nums[left]
        while left <= right:
            mid = (left + right) // 2
            if mid == len(nums) - 1 or nums[mid - 1] > nums[mid] < nums[mid + 1]:
                return nums[mid]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid - 1


if __name__ == '__main__':
    test_nums = [4,5,6,7,0,1,2]
    sol = Solution()
    print(sol.findMin(test_nums))
