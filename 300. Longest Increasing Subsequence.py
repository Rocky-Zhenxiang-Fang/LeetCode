from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
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