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

    def permute_2(self, nums: List[int]) -> List[List[int]]:
        """
        Idea: solve it recursively, as long as there are unused elements, put it at the next of the solution
        then pass the remaining elements to the next iteration, when all elements are used, one solution is found
        """
        res = []

        def recur(sub, remain) -> None:
            if not remain:  # nothing to add, one solution is found
                res.append(sub[:])  # deep copy
            else:
                for i in range(len(remain)):  # for each element in remain
                    sub.append(remain[i])  # add this item to the next element of answer
                    recur(sub, remain[:i] + remain[i + 1:])
                    sub.pop()  # remove the last item before adding another candidate

        recur([], nums)
        return res
