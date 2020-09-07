from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ind = len(nums) - k
        self.quickSelect(nums, 0, ind, len(nums) - 1)
        return nums[ind]

    def quickSelect(self, nums, start, k, end):
        """
        Instead of finding the right number, we sort the necessary part, and then return the right index
        """
        if start >= end:
            return
        pivot = nums[start]
        smaller = start + 1
        bigger = end
        while bigger >= smaller:
            if nums[smaller] <= pivot:
                smaller += 1
                continue
            if nums[bigger] > pivot:
                bigger -= 1
                continue
            nums[smaller], nums[bigger] = nums[bigger], nums[smaller]
            smaller += 1
            bigger -= 1
        nums[bigger], nums[start] = nums[start], nums[bigger]
        if k > bigger:
            return self.quickSelect(nums, bigger + 1, k, end)
        else:
            return self.quickSelect(nums, start, k, bigger - 1)


if __name__ == '__main__':
    sol = Solution()
    inp = [-1, 2, 0]
    k = 1
    print(sol.findKthLargest(inp, k))