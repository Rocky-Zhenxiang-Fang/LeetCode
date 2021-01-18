class Solution(object):
    def longestPalindrome(self, s) -> str:
        """
        Idea:
            A palindrome could be one of the two types:
                1. [a] + b + [a]
                2. [a] + b + b + [a]
            So we can check both types using each elements as b
        """
        ans = ""
        for i in range(len(s)):
            sub = self.find_palindrome(s, i, i)
            if len(sub) > len(ans):
                ans = sub
            sub = self.find_palindrome(s, i, i + 1)
            if len(sub) > len(ans):
                ans = sub
        return ans

    def find_palindrome(self, s, left, right) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return "".join(s[left + 1: right])


if __name__ == '__main__':
    s = "cbbd"
    sol = Solution()
    print(sol.longestPalindrome(s))
