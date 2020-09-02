from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        checked = set()
        self.dfs(res, nums, checked, [])
        return res

    def dfs(self, res, nums, checked, current):
        if set(current) in checked or len(nums) == 0:
            return
        else:
            res.append(current)
            checked.add(frozenset(current))
            for i in range(len(nums)):
                self.dfs(res, nums[:i] + nums[i + 1:], checked, current + [nums[i]])


if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))

