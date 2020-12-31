from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """
        Idea:
            Similar to 3Sum, but instead of finding all combinations, we only update
            their sum
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sub_sum = nums[i] + nums[j] + nums[k]
                if sub_sum == target:
                    return sub_sum
                elif abs(res - target) > abs(sub_sum - target):
                    res = sub_sum
                if sub_sum > target:
                    k -= 1
                else:
                    j += 1

        return res


if __name__ == '__main__':
    nums = [0, 2, 1, -3]
    target = 1
    sol = Solution()
    print(sol.threeSumClosest(nums, target))
