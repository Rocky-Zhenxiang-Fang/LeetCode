from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        if not num:
            return []
        self._dfs(res, num, 0, target, len(num))
        return res

    def _dfs(self, res, s, i, target, total_length):
        """
        :param res: stores all answer
        :param s: string containing numbers
        :param i: the number of iterations
        """
        if i == total_length - 1:
            s = s.replace(" ", "")
            if self._isVaild(s) and self.calculate(s) == target:
                res.append(s)
        else:
            for c in [" ", "+", "-", "*"]:
                next_str = s[:(2 * i + 1)] + c + s[(2 * i + 1):]
                self._dfs(res, next_str, i + 1, target, total_length)

    def _isVaild(self, s):
        s = "+" + s
        for i in range(len(s)):
            if s[i] in {"+", "-", "*"} and s[i + 1] == "0" and i + 2 != len(s) and s[i + 2] not in {"+", "-", "*"}:
                return False
        return True

    def calculate(self, s):
        stack, num, sign = [], 0, '+'

        for i in range(len(s)):
            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            if s[i] in '+-*' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop() * num)
                num = 0
                sign = s[i]

        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    num = ""
    target = 5
    print(sol.addOperators(num, target))
