from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, value in enumerate(nums):
            if nums[abs(value) - 1] < 0:
                res.append(abs(value))
            else:
                nums[abs(value) - 1] *= -1
            
        return res
        
        
if __name__ == '__main__':
    sol = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(sol.findDuplicates(nums))