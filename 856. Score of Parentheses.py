class Solution:
    def scoreOfParentheses(self, S):
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur


if __name__ == '__main__':
    s = "(()(()))"
    sol = Solution()
    print(sol.scoreOfParentheses(s))




