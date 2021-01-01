from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [" " for _ in range(len(indices))]
        for i in range(len(s)):
            res[indices[i]] = str(s[i])
        return "".join(res)


if __name__ == '__main__':
    s = "codeleet"
    indices = [4, 5, 6, 7, 0, 2, 1, 3]
    sol = Solution()
    print(sol.restoreString(s, indices))
