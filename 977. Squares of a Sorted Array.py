from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Idea:
            Two pointers, starting from the start and the end, put the one that have the bigger abs() into res
        """
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                res.append(nums[left] ** 2)
                left += 1
            else:
                res.append(nums[right] ** 2)
                right -= 1

        return res[::-1]


if __name__ == '__main__':
    nums = [-7,-3,2,3,11]
    sol = Solution()
    print(sol.sortedSquares(nums))