# Python3 program to find smallest multiple of
# a given number made of digits 0 and 9 only
import collections
from queue import Queue
from typing import List, Set


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self._dfs([], 0, target, candidates, 0, res)
        return res

    def _dfs(self, curr: List[int], curr_sum: int, target: int, remain: List[int], ptr: int, res: List[List[int]]):
        if curr_sum <= target:
            if curr_sum == target:
                res.append(curr[:])
            else:
                for i in range(ptr, len(remain)):
                    r = remain[i]
                    curr.append(r)
                    self._dfs(curr, curr_sum + r, target, remain, i, res)
                    curr.pop()

if __name__ == '__main__':
    sol = Solution()
    a = [2, 3, 6, 7]
    t = 7
    print(sol.combinationSum(a, t))
