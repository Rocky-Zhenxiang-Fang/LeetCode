class Solution(object):
    def generateParenthesis(self, n):
        """
        Backtracking problem:
            1. Decision:
                Choose to put a "(" or a ")"
            2. Constrains:
                1. We cannot have "(" more then n times
                2. We cannot have more ")" then "("
            3. Goal (base case of recursion):
                Have the length of the string equals to 2 * n
        """
        res = []
        if n == 0:
            return res
        self.dfs(res, "", n, 0, 0)
        return res

    def dfs(self, res, para: str, n: int, l: int, r: int) -> None:
        # Constrains:
        if l > n or r > l:
            return
        # Goal:
        if len(para) == n * 2:
            res.append(para)
            return
        # Decision:
        self.dfs(res, para + "(", n, l + 1, r)
        self.dfs(res, para + ")", n, l, r + 1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateParenthesis(3))