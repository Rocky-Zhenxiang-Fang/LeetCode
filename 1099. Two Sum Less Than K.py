from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        """
        Idea: sort the array first, then assign two pointers from the head and the end
            each iteration, find the first one that is smaller then k, compare it
            Note:
                if nums[start] + nums[end] = k, move the right one to let the sum smaller
        """
        nums.sort()
        res = -1
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < k:
                res = max(res, nums[left] + nums[right])
                left += 1
            else:
                right -= 1
        return res


if __name__ == '__main__':
    sol = Solution()
    nums = [10, 20, 30]
    k = 15
    print(sol.twoSumLessThanK(nums, k))
