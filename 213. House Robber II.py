from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.rob_one(nums[1:]), self.rob_one(nums[:-1]))

    def rob_one(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            # max(not taking the previous house, taking the previous house)
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]

if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    sol = Solution()
    print(sol.rob(nums))
