from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        """
        Idea:
            Find the maximum length of all shortest paths to all nodes in a weighted graph:
            Dijkstra !!
        """
        import heapq
        graph = [[] for _ in range(N + 1)]
        distance = [float("inf") for _ in range(N + 1)]
        distance[K] = 0
        distance[0] = -1
        visited = set()
        pq = [(0, K)]
        heapq.heapify(pq)
        for edge in times:
            graph[edge[0]].append((edge[1], edge[2]))

        while pq:
            dis, node = heapq.heappop(pq)
            if node not in visited:
                visited.add(node)
                for nei in graph[node]:
                    distance[nei[0]] = min(distance[nei[0]], nei[1] + distance[node])
                    heapq.heappush(pq, (distance[nei[0]], nei[0]))

        return max(distance)

if __name__ == '__main__':
    sol = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    N = 4
    K = 2
    print(sol.networkDelayTime(times, N, K))