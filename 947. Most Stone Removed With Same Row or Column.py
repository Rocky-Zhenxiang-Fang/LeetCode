
from typing import List
import random as rand

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # Idea: if a new stone is added, can I remove it from the previous stones?
        # DP problem
        stones.sort()
        res = 0
        for i in range(1, len(stones)):
            for j in range(0, i):
                curr = stones[j]
                prev = stones[i]
                if curr[0] == prev[0] or curr[1] == prev[1]:
                    res += 1
                    break
        return res


if __name__ == '__main__':
    sol = Solution()
    tests = [[[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 
            [[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 
            [[0, 0]]]
    results = [5, 3, 0]
    tests = zip(tests, results)
    for t, r in tests:
        rand.shuffle(t)
        if sol.removeStones(t) == r:
            print("test passed")
        else:
            print(t)
            print("test failed, should be " + str(r) + " but is " + str(sol.removeStones(t)))



#%%----------------------------------------------------------------
rows = [2, 2, 2]
cols = [2, 2, 2]

rows = [2, 1, 2]
cols = [2, 1, 2]




