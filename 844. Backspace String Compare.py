class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s_stack, t_stack = [], []
        for s in S:
            if s_stack and s == "#":
                s_stack.pop()
            elif s != "#":
                s_stack.append(s)
        for t in T:
            if t_stack and t == "#":
                t_stack.pop()
            elif t != "#":
                t_stack.append(t)
        return s_stack == t_stack


if __name__ == '__main__':
    S = "y#fo##f"
    T = "y#f#o##f"
    sol = Solution()
    print(sol.backspaceCompare(S, T))