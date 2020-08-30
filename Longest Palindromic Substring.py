class Solution(object):
    def longestPalindrome(self, s):
        """
        For any palindrome, middle of if will also be a palindrome
        Thus, starting from index i in s, the loop of finding max palindrome when
        s[i + l] != s[i - r] or s[i - l] != s[i + 1 + l]
        """
        maxPal = ""
        for i in range(len(s)):
            temp = self.maxPalindrome(s, i, i)
            if len(temp) > len(maxPal):
                maxPal = temp

            temp = self.maxPalindrome(s, i, i + 1)
            if len(temp) > len(maxPal):
                maxPal = temp
        return maxPal

    def maxPalindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1
        res = s[l + 1:r]
        return "".join(res)


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("cbbd"))