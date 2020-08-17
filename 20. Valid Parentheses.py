from builtins import str


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = []
        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                prev = stack.pop()

                if prev == "(" and ch != ")":
                    return False
                if prev == "[" and ch != "]":
                    return False
                if prev == "{" and ch != "}":
                    return False
        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    sol = Solution()
    strInput = "()"
    print(sol.isValid(strInput))
    strInput = "()[]{}"
    print(sol.isValid(strInput))
    strInput = "(]"
    print(sol.isValid(strInput))
    strInput = "([)]"
    print(sol.isValid(strInput))
    strInput = "{[]}"
    print(sol.isValid(strInput))
