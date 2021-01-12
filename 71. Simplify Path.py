class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        res = []
        for p in paths:
            if p == "." or p == "":
                continue
            elif p == "..":
                if len(res) > 0:
                    res.pop()
            else:
                res.append(p)
        return "/" + "/".join(res)


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

