from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        topological sort
        """
        res = []
        graph = [[] for _ in range(numCourses)]
        in_edges = [0 for _ in range(numCourses)]
        zero_input = []
        for p in prerequisites:
            graph[p[1]].append(p[0])
            in_edges[p[0]] += 1
        for i in range(len(in_edges)):
            if in_edges[i] == 0:
                zero_input.append(i)
        while zero_input:
            curr = zero_input.pop()
            res.append(curr)
            for nei in graph[curr]:
                in_edges[nei] -= 1
                if in_edges[nei] == 0:
                    zero_input.append(nei)

        return res if len(res) == numCourses else []


if __name__ == '__main__':
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    sol = Solution()
    print(sol.findOrder(numCourses, prerequisites))
