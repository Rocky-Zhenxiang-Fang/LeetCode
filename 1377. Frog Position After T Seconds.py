from typing import List
import collections


class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        """
        Idea:
            We can know the possibility of getting to any node by possibility of parent / number of siblings
            Since there are no direction and we don't visit the same node, use a set
            Use a BFS to ensure that we don't run out of time
            If the frog is on the target node and there still have time and it still have childrens, return 0
            Otherwise, return the possibility
            return 0 if the target cannot be reached in time
        """
        graph = self._build_graph(n, edges)
        visited = set()
        que = collections.deque([(1, t, 1.0)])
        while que:
            curr_node, time, poss = que.pop()
            if time < 0:
                break
            if curr_node not in visited:
                visited.add(curr_node)
                if curr_node == target:
                    if time == 0:
                        return poss
                    else:
                        for nei in graph[curr_node]:
                            if nei not in visited:
                                return 0
                        return poss
                else:
                    children = [child for child in graph[curr_node] if child not in visited]
                    for nei in children:
                        que.appendleft((nei, time - 1, poss / len(children)))

        return 0

    def _build_graph(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n + 1)]  # remember the n in 1 indexed
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        return graph


if __name__ == '__main__':
    sol = Solution()
    n = 9
    edges = [[2, 1], [3, 1], [4, 2], [5, 3], [6, 5], [7, 4], [8, 7], [9, 7]]
    t = 1
    target = 8
    print(sol.frogPosition(n, edges, t, target))
