class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        BFS, Change visited cell as 0
        """
        from collections import deque
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        que = deque([((0, 0), 1)])
        while que:
            curr, dis = que.pop()
            if 0 <= curr[0] < len(grid) and 0 <= curr[1] < len(grid) and grid[curr[0]][curr[1]] == 0:
                grid[curr[0]][curr[1]] = 1
                if curr == (len(grid) - 1, len(grid) - 1):
                    return dis
                else:
                    neighbors = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
                    for n in neighbors:
                        que.appendleft(((curr[0] + n[0], curr[1] + n[1]), dis + 1))
        return -1









