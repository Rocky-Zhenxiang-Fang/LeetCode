from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # Idea:
        # All roads should head towards 0 since the number of roads are limited
        # Start from 0, if there is anyroad outgoing, flip it, mark the checked neighbor as "checked"
        # Do DFS for each "checked" and treat them as 0, do the samething
        res = 0
        stack = [(0, 0)]
        out_going_graph = [[] for _ in range(n)]
        in_comming_graph = [[] for _ in range(n)]
        for c in connections:
            out_going_graph[c[0]].append(c[1])
            in_comming_graph[c[1]].append(c[0])
        visited = set()
        while stack: 
            parent, curr = stack.pop()
            visited.add(curr)
            out_neighbors = out_going_graph[curr]
            in_neighbors = in_comming_graph[curr]
            for nei in out_neighbors:
                if nei not in visited:
                    stack.append((curr, nei))
                if nei != parent:
                    res += 1
            for nei in in_neighbors:
                if nei not in visited:
                    stack.append((curr, nei))
        return res
            

if __name__ == '__main__':
    sol = Solution()
    arr = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    print(sol.minReorder(6, arr))