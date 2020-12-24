from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        min_length = float("inf")
        local_sum = 0
        start, end = 0, 0
        while start < len(nums):
            local_sum += nums[start]
            start += 1
            while local_sum >= s:
                min_length = min(min_length, start - end)
                local_sum -= nums[end]
                end += 1
        return min_length if min_length != float("inf") else 0


if __name__ == '__main__':
    s = 11
    nums = [1, 2, 3, 4, 5]
    sol = Solution()
    print(sol.minSubArrayLen(s, nums))