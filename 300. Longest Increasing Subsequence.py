from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
<<<<<<< HEAD
        res = 0
        for i in range(len(nums)):
            curr = nums[i]
            tmp = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > curr:
                    tmp += 1
                    curr = nums[j]
            res = max(res, tmp)
        return res
        

if __name__ == "__main__":
    arr = [10,9,2,5,3,4]
    sol = Solution()
    print(sol.lengthOfLIS(arr))
=======
        """
        From https://www.youtube.com/watch?v=fV-TF4OvZpk
        for each number in nums, we see how can it extend previous subsequences, and store the
        maximum of them into the box
        """
        dp = [1 for _ in range(len(nums))]
        for i in range(len(dp)):
            tmp = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    tmp = max(dp[j] + 1, tmp)
            dp[i] = tmp
        return max(dp)


if __name__ == '__main__':
    sol = Solution()
    arr = [-1, 3, 4, 5, 2, 2, 2, 2]
    print(sol.lengthOfLIS(arr))


>>>>>>> 5dfe6b52fa7b3e47a0bc2a3dff0244d55ef79150
