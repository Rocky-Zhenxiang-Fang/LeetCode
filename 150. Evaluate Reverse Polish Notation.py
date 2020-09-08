from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(a - b)
                elif t == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
        return stack[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN(["2", "1", "+", "3", "*"]))