class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if row > 0 and grid[row - 1][col] == 1: continue
                    if col > 0 and grid[row][col - 1] == 1: continue
                    ans += 1
        return ans


if __name__ == '__main__':
    g = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    sol = Solution()
    print(sol.numIslands(g))
