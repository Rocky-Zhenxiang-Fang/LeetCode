from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        DFS can reach all node in one components, so just count how many dfs needed
        """
        visited = set()
        stack = []
        graph = [[] for _ in range(n)]
        res = 0
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        for i in range(n):
            if i not in visited:
                stack.append(i)
                res += 1
                while stack:
                    curr = stack.pop()
                    if curr not in visited:
                        visited.add(curr)
                        for nei in graph[curr]:
                            stack.append(nei)
        return res


if __name__ == '__main__':
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    print(sol.countComponents(n, edges))
