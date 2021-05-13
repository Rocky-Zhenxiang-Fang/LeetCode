from typing import List


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        return self._dfs(values, 0)

    def _dfs(self, values: List[int], curr: int) -> int:
        if len(values) == 3:
            return values[0] * values[1] * values[2] + curr
        else:
            res = float("inf")
            for i in range(len(values)):
                res = min(res, self._dfs(values[:i] + values[i + 1:],
                                         curr + values[i - 1] * values[i] * values[(i + 1) % len(values)]))
            return res


if __name__ == '__main__':
    test = [3, 7, 4, 5]
    sol = Solution()
    print(sol.minScoreTriangulation(test))