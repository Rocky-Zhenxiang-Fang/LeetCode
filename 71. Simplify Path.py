from typing import Tuple


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        idx = 0
        while idx < len(path):
            directory, idx = self._get_next_directory(path, idx)
            if directory == "..":
                if stack:
                    stack.pop()
            elif directory == ".":
                continue
            elif len(directory) != 0:
                stack.append(directory)
        return "/" + "/".join(stack)
        
        
    def _get_next_directory(self, path: str, start: int) -> Tuple[str, int]:
        """
        Given a path and a start, return the next directory and the next start
        """
        res = []
        while start < len(path):
            if path[start] != "/":
                res.append(path[start])
            else:
                if res:
                    break
            start += 1
        return "".join(res).strip(), start


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

