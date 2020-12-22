from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Idea, when appending a char, see if it can combine to any previous segmentation and still form a word
        For example, assuming that we are at index 5 and we already know that s[:3] can form a valid set, if s[4:5] can
        form a valid set, then dp[i] will be true
        """
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]     # the first one is True so that each iteration will search s[:i]
        dp[0] = True
        for i in range(1, len(dp)):
            for j in range(i):
                if dp[j]:
                    print(s[j: i])
                    if s[j: i] in wordSet:
                        dp[i] = True
                        break
        return dp[-1]


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    sol = Solution()
    print(sol.wordBreak(s, wordDict))

