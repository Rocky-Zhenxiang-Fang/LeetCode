from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        for i in range(1, len(nums), 2):
            if i != len(nums) - 1:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]


if __name__ == '__main__':
    sol = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    sol.wiggleSort(arr)
    print(arr)