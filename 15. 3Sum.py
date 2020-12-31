from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Idea: try to reduce it into two sum problem
            it will have n two sum problem, so the total run time is O(n^2)
            Since the runtime is already bigger then O(nlogn), sort does not change
            asymptotic run time.
            For i in range(len(nums)):
                two sum(nums[i:], 0 - nums[i])
            use two pointer to solve two sum pointer
        """
        added = set()
        nums.sort()
        start = 0

        def two_sum(head: int, target):
            sub_start, sub_end = head, len(nums) - 1
            while sub_start < sub_end:
                if nums[sub_start] + nums[sub_end] == target:
                    added.add(tuple(sorted([-target, nums[sub_start], nums[sub_end]])))
                    sub_start += 1
                    sub_end -= 1
                elif nums[sub_start] + nums[sub_end] < target:
                    sub_start += 1
                else:
                    sub_end -= 1

        while nums[start] <= 0:
            two_sum(start + 1, 0 - nums[start])
            start += 1

        return list(added)


if __name__ == '__main__':
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
