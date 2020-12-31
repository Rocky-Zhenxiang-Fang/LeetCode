from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        Idea: reduce to three sum, then reduce to two sum
        """
        if len(nums) < 4:
            return []
        res = set()
        ans = []
        nums.sort()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                k, z = j + 1, len(nums) - 1
                while k < z:
                    sub_sum = nums[i] + nums[j] + nums[k] + nums[z]
                    if sub_sum == target:
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], nums[z]])))
                        while k < z and nums[k] == nums[k + 1]:
                            k += 1
                        while k < z and nums[z] == nums[z - 1]:
                            z -= 1
                        k += 1
                        z -= 1
                    elif sub_sum < target:
                        k += 1
                    else:
                        z -= 1
        for r in res:
            ans.append(list(r))
        return ans


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(sol.fourSum(nums, target))


