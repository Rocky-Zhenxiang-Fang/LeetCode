class Solution:
    from typing import List, Set, Tuple

    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Backtracking problem:
            1. Decision:
                Add a number from nums into a list
            2. Constrains:
                1. A number cannot be used twice
                2. Not need to check the same sequence twice
            3. Goal (base case of recursion):
                No remaining nums left
        """
        res = []
        checked = set()
        if len(nums) == 0:
            return res
        self.dfs(res, checked, nums, [])
        return res

    def dfs(self, res: List[int], checked: Set[Tuple[int]], nums: List[int], current: List[int]) -> None:
        if tuple(current) in checked:
            return
        else:
            checked.add(tuple(current))
        if len(nums) == 0:
            res.append(current)
            return
        for i in range(len(nums)):
            self.dfs(res, checked, nums[:i] + nums[i + 1:], current + [nums[i]])
