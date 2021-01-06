class Solution(object):
    def letterCombinations(self, digits):
        """
        All permutation need to be passed, backtracking needed
        """
        res = []
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        if not digits:
            return res
        def dfs(sub: str, remaining: str, mapping):
            if not remaining:  # base case
                res.append(sub)
            else:
                for c in mapping[remaining[0]]:
                    dfs(sub + c, remaining[1:], mapping)

        dfs("", digits, mapping)
        return res


if __name__ == '__main__':
    dig = "23"
    sol = Solution()
    print(sol.letterCombinations(dig))
