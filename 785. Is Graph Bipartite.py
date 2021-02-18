from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        from collections import deque
        visited = [-1] * len(graph)  # store node: set number
        que = deque()
        unvisited = set([i for i in range(len(graph))])
        while unvisited:
            head = unvisited.pop()
            que.append(head)
            visited[head] = 0
            while que:
                curr = que.pop()
                for nei in graph[curr]:
                    if visited[nei] != -1:
                        if visited[curr] == visited[nei]:
                            return False
                    else:
                        que.appendleft(nei)
                        unvisited.remove(nei)
                        visited[nei] = 1 if visited[curr] == 0 else 0
        return True


if __name__ == '__main__':
    gra = [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    sol = Solution()
    print(sol.isBipartite(gra))
