from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Idea:
            When adding a char, see if s[:i] belongs to a word
            Also, assuming that there a s[:j] that form a string, then we also want to check if s[j + 1: i] forms a word
        """
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            for j in range(i + 1):
                if dp[j] and s[j: i + 1] in words:
                    dp[i + 1] = True
                    break
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    s_2 = "a"
    w_2 = ["a"]
    sol = Solution()
    print(sol.wordBreak(s_2, w_2))

