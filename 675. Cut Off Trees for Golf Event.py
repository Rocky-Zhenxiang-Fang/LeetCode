from typing import List, Tuple
from collections import deque
import heapq


class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        """
        Idea:
            Since the order is defined, we need to follow the order and find out the cost of each path
        Alg:
            First, create a list of (v, r, c) where v = forest[r][c] and sorted by v
            Then, starting from (0, 0), add up the cost between each path using BFS
            If cannot find a path, return -1
        """
        trees = []
        res = 0
        for r in range(len(forest)):
            for c in range(len(forest[0])):
                if forest[r][c] > 0:
                    trees.append((forest[r][c], r, c))
        trees.sort()
        start = (0, 0)
        for i in range(len(trees)):
            end = trees[i]
            path_len = self.a_star(forest, start, (end[1], end[2]))
            if path_len == -1:
                return -1
            else:
                res += path_len
            start = (end[1], end[2])
        return res

    def a_star(self, forest: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
        heap = [(start, 0, 0)]  # stores (node, cost, path_len)
        heapq.heapify(heap)
        cost = {start: 0}   # stores (node: cost)
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        while heap:
            curr, path_cost, path_len = heapq.heappop(heap)
            if curr == end:
                return path_len
            else:
                for m in moves:
                    nr, nc = curr[0] + m[0], curr[1] + m[1]
                    if 0 <= nr < len(forest) and 0 <= nc < len(forest[0]) and forest[nr][nc] > 0:
                        ncost = path_len + 1 + abs(end[0] - nr) + abs(end[1] - nc)
                        if ncost < cost.get((nr, nc), float("inf")):
                            cost[(nr, nc)] = ncost
                            heapq.heappush(heap, ((nr, nc), ncost, path_len + 1))

        return -1
