class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = [False for _ in range(len(s))]
        prev_count = 0
        paired = 0
        for i in range(len(s)):
            if s[i] == "(":
                prev_count += 1
                valid[i] = True
            elif s[i] == ")":
                if prev_count > 0:
                    prev_count -= 1
                    paired += 1
                    valid[i] = True
                else:
                    valid[i] = False
            else:
                valid[i] = True
        prev_count = 0
        for j in range(len(s) - 1, -1, -1):
            if valid[j]:
                if s[j] == ")":
                    prev_count += 1
                elif s[j] == "(":
                    if prev_count <= 0:
                        valid[j] = False
                    else:
                        prev_count -= 1
        res = []
        for i in range(len(valid)):
            if valid[i]:
                res.append(s[i])
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    s = "))(("
    print(sol.minRemoveToMakeValid(s))