class Solution:
    def calculate(self, s):
        """
        Idea:
            We want to do two rounds, first for * /, second for +-. The second can be done by using sum(stack)
            Keep a stack of all integers, return the sum of stack
            if operator is +-, push num or -num in stack
            if operator is */, before pushing it into the stack, we need to combine it with the last element
        """
        stack, num, sign = [], 0, "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in {"+", "-", "*", "/"} or i == len(s) - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":       # python // is floor, but we want it truncate to 0
                    stack.append(int(stack.pop()/num))
                num = 0
                sign = s[i]
        return sum(stack)


if __name__ == '__main__':
    sol = Solution()
    s = "19 + 23 - 47 * 100 / 20 + 5"
    print(sol.calculate(s))
