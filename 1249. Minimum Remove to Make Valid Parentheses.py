class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        Idea:
            If a right parentheses is valid, there must be at least one remaining left parentheses for it to pair with
            Vice, versa.
            Do two iterations:
                1.
                    when encounter a left parentheses, increase left counter
                    when encounter a right paretheses, only include it if there are remaining left
                2.
                    Do the same thing, but remove left parentheses
        """
        res = ""
        real_res = ""
        left = 0
        paired = 0
        for c in s:
            if c == "(":
                res += c
                left += 1
            elif c == ")":
                if left > 0:
                    res += c
                    left -= 1
                    paired += 1
            else:
                res += c

        for r in res:
            if r == "(":
                if paired <= 0:
                    continue
                else:
                    paired -= 1
            real_res += r

        return real_res


if __name__ == '__main__':
    sol = Solution()
    s = "lee(t(c)o)de)"
    print(sol.minRemoveToMakeValid(s))