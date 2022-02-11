from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        res = float("inf")
        min_ptr = 0
        max_ptr = -4
        while min_ptr <= 3:
            res = min(res, abs(nums[max_ptr] - nums[min_ptr]))
            max_ptr += 1
            min_ptr += 1
        return res 
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [20,66,68,57,45,18,42,34,37,58]
    print(sol.minDifference(nums))
        