from typing import List, Set


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        By removing a bridge, there are at least a pair of nodes cannot reach each other
            Thus, bridge cannot be in a circle. Also, if two nodes are not in cycle, by removing the edge between them,
            they will be disconnected
        How can we see if a edge is in a circle:
            Assuming that we are walking down a path, if we can walk to a place that is previously seen but not walking
            back, this means that this is a cycle. In this case, we can walk back to the intersection and all paths are
            not bridge.
            Otherwise, this is a bridge
        """
        graph = [[] for _ in range(n)]  # adj_list of the graph
        lowest = [0 for _ in range(n)]  # the farthest parent that this node can reach directly
        index = [0 for _ in range(n)]  # stores the index of the node on the path
        visited = set()
        res = []
        for c in connections:
            graph[c[0]].append(c[1])
            graph[c[1]].append(c[0])

        self._dfs(0, -1, visited, lowest, index, 0, graph, res)
        return res

    def _dfs(self, node: int, parent: int, visited: Set[int], lowest: List[int], index: List[int], curr_level: int,
             graph: List[List[int]], res: List[List[int]]):
        visited.add(node)
        index[node] = curr_level
        lowest[node] = curr_level  # in here, we only know that this node can be reach from its parent
        for nei in graph[node]:
            if nei == parent:
                continue
            if nei not in visited:
                self._dfs(nei, node, visited, lowest, index, curr_level + 1, graph,
                          res)  # if haven't visited this neighbor, add it into this path
            lowest[node] = min(lowest[node], lowest[
                nei])  # after the neighbor is analyzed, we can know that it we can find a shorter path
            if lowest[nei] > curr_level:  # if the lowest node that this neighbor can reach is not smaller then myself, no cycle
                res.append([node, nei])


if __name__ == '__main__':
    sol = Solution()
    g = [[0, 1], [1, 2], [2, 0], [1, 3]]
    print(sol.criticalConnections(4, g))
