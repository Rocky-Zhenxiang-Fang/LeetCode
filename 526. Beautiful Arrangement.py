from typing import List


class Solution:
    def countArrangement(self, n: int) -> int:
        """
        Backtracking
            Do dfs, and add one if find a permutation
            stop early if found a wrong number is placed
        """
        self.ans = 0
        nums = [i for i in range(1, n + 1)]
        self._dfs([], nums, n)
        return self.ans

    def _dfs(self, sub, remaining, target):
        if sub and not ((len(sub)) % sub[-1] == 0 or sub[-1] % (len(sub)) == 0):
            return
        if len(sub) == target:
            self.ans += 1
        else:
            for i in range(len(remaining)):
                self._dfs(sub + [remaining[i]], remaining[:i] + remaining[i + 1:], target)


if __name__ == '__main__':
    n = 2
    sol = Solution()
    print(sol.countArrangement(n))
