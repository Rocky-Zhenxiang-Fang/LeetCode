class Solution:
    def simplifyPath(self, path: str) -> str:
        dir = path.split("/")
        stack = []
        for ch in dir:
            if ch == "..":
                if len(stack) != 0:
                    stack.pop()
            elif ch != "." and ch != "":
                stack.append(ch)

        res = "/" + "/".join(stack)
        return res


if __name__ == '__main__':
    sol = Solution()
    strInput = "/home/"
    print(sol.simplifyPath(strInput))
    strInput = "/../"
    print(sol.simplifyPath(strInput))
    strInput = "/home//foo/"
    print(sol.simplifyPath(strInput))
    strInput = "/a/./b/../../c/"
    print(sol.simplifyPath(strInput))
    strInput = "/a/../../b/../c//.//"
    print(sol.simplifyPath(strInput))
    strInput = "/a//b////c/d//././/.."
    print(sol.simplifyPath(strInput))

