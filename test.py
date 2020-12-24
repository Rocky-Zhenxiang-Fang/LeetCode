# This file is used to review done questions

# Definition for a binary tree node.
from typing import List

import DS


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
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


if __name__ == '__main__':
    nums = [1, 2, 3]
    sol = Solution()
    print(sol.permute(nums))
