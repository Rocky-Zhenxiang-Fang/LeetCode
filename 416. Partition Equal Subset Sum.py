from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        idea: does this array has a subset that sums to sum(num) / 2
        """
        target = sum(nums) // 2
        if target - sum(nums) / 2 != 0:  # sum of interget cannot be a float number
            return False
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]
        for row in range(len(dp)):
            dp[row][0] = 1  # empty set will sum to zero
        for element in range(1, len(dp)):
            for tar in range(1, len(dp[0])):
                if tar - nums[element - 1] >= 0:
                    dp[element][tar] = dp[element - 1][tar] or dp[element - 1][tar - nums[element - 1]]
                else:
                    dp[element][tar] = dp[element - 1][tar]
        return True if dp[-1][-1] == 1 else False