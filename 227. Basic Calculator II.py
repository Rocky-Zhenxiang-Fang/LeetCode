class Solution:
    def calculate(self, s: str) -> int:
        curr, stack, sign = 0, [], "+"
        for i, ch in enumerate(s):
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if ch in {"+", "-", "*", "/"} or i == len(s) - 1:
                if sign == "+":
                    stack.append(curr)
                elif sign == "-":
                    stack.append(-curr)
                elif sign == "*":
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                sign = ch
                curr = 0

        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    s = "3+2*2"
    print(sol.calculate(s))
