from typing import List



class Solution:
    # Not Working
    # def canJump(self, nums: List[int]) -> bool:
    #     currID: int = 0  # current location
    #     while currID < len(nums) - 1:
    #         step = nums[currID]
    #         if step == 0:
    #             return False
    #         if step + currID >= len(nums) - 1:
    #             return True
    #         maxItem = 0
    #         maxId = 0
    #         for i, item in enumerate(nums[currID + 1: currID + step + 1]):
    #             if item >= maxItem:
    #                 maxId = i
    #                 maxItem = item
    #
    #         currID = currID + maxId + 1
    #
    #     return True
    def canJump(self, nums: List[int]) -> bool:
        """
        Solved by DP
        """
        farest = 0
        for i in range(len(nums)):
            if i > farest:
                return False
            farest = max(farest, i + nums[i])

        return True

    def canJump2(self, nums: List[int]) -> bool:
        """
        If any 0 is presented, we want to see if there is a way to get pass a pole
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                gap = 1
                while nums[i] < gap:
                    gap += 1
                    i -= 1
                    if i < 0: return False
        return True


if __name__ == '__main__':
    sol = Solution()
    nums = [5,9,3,2,1,0,2,3,3,1,0,0]
    print(sol.canJump(nums))
    nums = [2, 0, 0]
    print(sol.canJump(nums))
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))
    nums = [3,2,1,0,4]
    print(sol.canJump(nums))
