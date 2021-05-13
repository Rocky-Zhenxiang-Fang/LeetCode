import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Idea:
            BFS, do until no fresh orange exist
        """
        que = collections.deque()
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        freshes = 0
        time = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    que.append((row, col))
                elif grid[row][col] == 1:
                    freshes += 1
        while que:
            n = len(que)
            time += 1
            for _ in range(n):
                row, col = que.pop()
                for m in moves:
                    r, c = row + m[0], col + m[1]
                    if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
                        freshes -= 1
                        grid[r][c] = 2
                        que.appendleft((r, c))
        return time if freshes == 0 else -1


if __name__ == '__main__':
    sol = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(sol.orangesRotting(grid))
