from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Idea:
            The input array is kinda sorted, with the both side bigger then the middle
            Thus, we can make the result array and fill it backwards
        """
        res = [0 for _ in range(len(nums))]
        left, right, ptr = 0, len(res) - 1, len(res) - 1
        while ptr >= 0:
            if nums[left] ** 2 > nums[right] ** 2:
                res[ptr] = nums[left] ** 2
                left += 1
            else:
                res[ptr] = nums[right] ** 2
                right -= 1
            ptr -= 1
        return res


if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    sol = Solution()
    print(sol.sortedSquares(nums))