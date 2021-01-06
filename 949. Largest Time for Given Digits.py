from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        """
        Idea:
            Generate all permutation, and check it
        """
        self.ans = ["0", "0", "0", "0"]
        self._dfs([], arr)
        res = "".join(self.ans)
        return res[:2] + ":" + res[2:] if res != "0" else ""

    def _dfs(self, sub: List[int], remaining: List[int]):
        if len(sub) == 4:
            sub_int = int("".join(map(str, sub)))
            ans_int = int("".join(map(str, self.ans)))
            if sub_int < 2400 and (sub_int % 100) < 60:
                if sub_int > ans_int:
                    self.ans = sub
        else:
            for i in range(len(remaining)):
                self._dfs(sub + [remaining[i]], remaining[:i] + remaining[i + 1:])


if __name__ == '__main__':
    sol = Solution()
    arr = [0, 0, 0, 0]
    print(sol.largestTimeFromDigits(arr))
