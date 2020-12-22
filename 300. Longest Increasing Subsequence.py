from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Idea: in each iteration, decide if it wants to connect to previous components
        """
        dp = [0 for _ in range(len(nums))]  # dp stores the maximum sum of the subarray that contains itself
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])  # if connect to previous components can increase sum, do it
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(arr))
