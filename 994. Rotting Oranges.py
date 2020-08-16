import collections
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def twoNearBy(row, col):
            can = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
            for i in can:
                if 0 <= i[0] < len(grid) and 0 <= i[1] < len(grid[0]):
                    if grid[i[0]][i[1]] == 2:
                        return True

            return False

        minutes = 0
        thisQ = collections.deque()
        reNewQ = collections.deque()
        nextQ = collections.deque()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    thisQ.append((row, col))
        if len(thisQ) == 0: return minutes

        while True:
            qSize = len(thisQ)
            while thisQ:
                ind = thisQ.popleft()
                if not twoNearBy(ind[0], ind[1]):
                    nextQ.append(ind)
                else:
                    reNewQ.append(ind)
            while reNewQ:
                ind = reNewQ.popleft()
                grid[ind[0]][ind[1]] = 2
            minutes += 1
            if len(nextQ) == 0: return minutes
            if len(nextQ) == qSize: return -1
            thisQ = nextQ.copy()
            nextQ.clear()


if __name__ == '__main__':
    sol = Solution()
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print(sol.orangesRotting(grid))
