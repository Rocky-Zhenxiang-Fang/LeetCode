from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """
        Idea:
            Do a DFS, at each time, add the time needed to send message from manger to employee. When reaches a leaf
            return its result
        """
        from collections import defaultdict

        def dfs(worker: int) -> int:
            res = 0
            time = informTime[worker] if worker != -1 else 0
            for sub in employee[worker]:
                res = max(res, time + dfs(sub))
            return res

        employee = defaultdict(list)
        for i in range(len(manager)):
            employee[manager[i]] = employee[manager[i]] + [i]
        return dfs(-1)


if __name__ == '__main__':
    sol = Solution()
    n = 4
    headID = 2
    manager = [3, 3, -1, 2]
    informTime = [0, 0, 162, 914]
    print(sol.numOfMinutes(n, headID, manager, informTime))
