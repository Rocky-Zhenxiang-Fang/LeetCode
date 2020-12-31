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
        start, end = 0, len(nums) - 1
        biggest = -1
        while start != end:
            if nums[start] + nums[end] >= k:
                end -= 1
            else:
                biggest = max(biggest, nums[start] + nums[end])
                start += 1
        return biggest


if __name__ == '__main__':
    sol = Solution()
    nums = [10,20,30]
    k = 15
    print(sol.twoSumLessThanK(nums, k))


