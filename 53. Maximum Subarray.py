from typing import List


class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     """
    #     Time Limit Exceeded
    #     Time Complexity: O(n**2)
    #     :param nums:
    #     :return:
    #     """
    #     maxRes = nums[0]
    #     for i in range(len(nums)):
    #         subSum = 0
    #         for j in range(i, len(nums)):
    #             subSum += nums[j]
    #             maxRes = max(maxRes, subSum)
    #     return maxRes

    def maxSubArray(self, nums: List[int]) -> int:
        """
        1. Iterate the entire array
        2. When at nums[i], if the prefix to nums[i - 1] is negative, ignore the prefix
        3. Update maxRes so that it is the biggest number
        """
        maxRes = nums[0]
        prefix = 0
        for i in range(1, len(nums)):
            prefix += nums[i - 1]
            if prefix < 0:
                prefix = 0
            maxRes = max(maxRes, prefix + nums[i])
        return maxRes


if __name__ == '__main__':
    sol = Solution()
    num = [-1]
    print(sol.maxSubArray(num))
