from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        faced = None
        place = 0
        unique = 0
        while unique != len(nums):
            if nums[unique] != faced:
                nums[unique], nums[place] = nums[place], nums[unique]
                faced = nums[place]
                place += 1
            unique += 1
        return place


if __name__ == '__main__':
    sol = Solution()
    arr = [0,0,1,1,1,2,2,3,3,4]
    print(sol.removeDuplicates(arr))
    print(arr)

