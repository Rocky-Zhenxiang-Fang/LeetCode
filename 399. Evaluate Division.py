from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i, e in enumerate(equations):
            graph[e[1]] = graph.get(e[1], []) + [(e[0], values[i])]
            graph[e[0]] = graph.get(e[0], []) + [(e[1], 1 / values[i])]
        res = []
        for q in queries:
            res.append(self._find_ratio(graph, q[1], q[0]))
        return res
        
        
    def _find_ratio(self, graph, source, dist) -> float:
        if source not in graph or dist not in graph:
            return -1.0
        stack = [(source, 1.0)]
        visited = set()
        while stack:
            curr, ratio = stack.pop()
            visited.add(curr)
            if curr == dist:
                return ratio
            else:
                neighbors = graph[curr]
                for n in neighbors:
                    if n[0] not in visited:
                        stack.append((n[0], ratio * n[1]))
        return -1.0
        
        
if __name__ == '__main__':
    sol = Solution()
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(sol.calcEquation(equations, values, queries))