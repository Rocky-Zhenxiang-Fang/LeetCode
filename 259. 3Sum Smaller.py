from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        """
        Idea: Similar to closest, however, this time only update ans if the sum is smaller then target
            If we fix i and j, we can find k from the right end, as long as the sum is smaller then target
            all indices between [i + 1, k] can be put in the last cell
            for i + 1, we dont need to reset k since nums is sorted
        """
        if len(nums) < 3:
            return 0
        ans = 0
        nums.sort()
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sub_sum = nums[i] + nums[j] + nums[k]
                if sub_sum < target:
                    ans += k - j
                    j += 1
                else:
                    k -= 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [3, 1, 0, -2]
    target = 4
    print(sol.threeSumSmaller(nums, target))

