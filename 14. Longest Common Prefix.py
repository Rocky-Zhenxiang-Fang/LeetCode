from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = float("inf")
        if len(strs) == 0:
            return ""
        for s in strs:
            if len(s) == 0:
                return ""
            else:
                minLen = min(len(s), minLen)

        ans = ""
        for i in range(minLen):
            tar = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != tar:
                    return ans
            ans += tar
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["a"]))