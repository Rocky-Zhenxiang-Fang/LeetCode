from typing import List
import heapq

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        """
        Idea:
            For any item, if there are elements on its both side that is smaller then it, return True
            Doing a linear scan from left, we can find if there is a number smaller then current number by keeping a smallest
            Similarly, we can do a linear scan from right, as long as the there is a number between left and curr, return True
            The right scan, we keep a stack that stores all possible rights, we know that left is increasing from right to left
            Thus, if a number is smaller then current small, then it will never become useful, if can be removed
        """
        dp = [float("inf")] * len(nums)
        smallest = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > smallest:
                dp[i] = smallest
            else:
                smallest = nums[i]

        rights = []
        for i in range(len(nums) - 1, -1, -1):
            if dp[i] != float("inf"):
                while rights and rights[-1] <= dp[i]:
                    rights.pop()
                if rights and rights[-1] < nums[i]:
                    return True
            rights.append(nums[i])
        return False


if __name__ == '__main__':
    sol = Solution()
    arr = [1,2,3,4]
    print(sol.find132pattern(arr))