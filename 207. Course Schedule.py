from typing import List
import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Idea:
            Using Topological sort
        """
        in_degree = [0] * numCourses
        pres = collections.defaultdict(list)
        visited = set()
        zero_ins = set()
        for p in prerequisites:
            in_degree[p[1]] += 1
            pres[p[0]] = pres.get(p[0], []) + [p[1]]
        zero_ins = set([i for i in range(len(in_degree)) if in_degree[i] == 0])
        while zero_ins:
            curr = zero_ins.pop()
            if curr not in visited:
                visited.add(curr)
                for nei in pres[curr]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        zero_ins.add(nei)
        return len(visited) == numCourses


if __name__ == '__main__':
    sol = Solution()
    num = 2
    pre = [[1, 0]]
    print(sol.canFinish(num, pre))
