from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0: return [[]]
        res, state, r = [], [-1 for _ in range(n)], 0

        def add(state, r) -> bool:
            """
            Adds a value to state[] at r index,
            It should follows the rule of N-Queen
            If cannot, return False
            """
            for i in range(r):
                if abs(state[r] - state[i]) == r - i or state[i] == state[r]:
                    return False

            return True

        def getOneAns(state) -> List:
            """
            Interprets state into a board and add it into res
            """
            ans: List[str] = ["." for _ in range(n)]
            for i, c in enumerate(state):
                ans[i] = "." * c + "Q" + "." * (n - c - 1)
            return ans

        def dfs(state, r, res):
            if r == len(state):
                res.append(getOneAns(state))
                return
            for i in range(n):
                state[r] = i
                if add(state, r):
                    r += 1
                    dfs(state, r, res)
                    r -= 1

        dfs(state, r, res)
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.solveNQueens(15))