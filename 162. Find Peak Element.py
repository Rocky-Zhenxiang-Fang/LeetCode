from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def findPeak(start, end):
            if start == end:
                return start
            mid = (start + end) // 2
            if mid == 0:
                if nums[mid] > nums[mid + 1]:
                    return mid
            if mid == len(nums) - 1:
                if nums[mid] > nums[mid - 1]:
                    return mid
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            if nums[mid + 1] > nums[mid]:
                return findPeak(mid + 1, end)
            else:
                return findPeak(start, mid - 1)
        return findPeak(0, len(nums) - 1)


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2]
    print(sol.findPeakElement(arr))