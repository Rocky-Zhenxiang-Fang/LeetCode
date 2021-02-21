class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        """
        Idea:
            This problem cannot be optimized to less then O(n**2) since there are no dependency between sub-problems
            For a Palindromic, it is [a] + b + [a'] or  [a] + b + b + [a']
            Create a helper function with two pointers, when two pointers are not equal, return the length
        """
        res = ""
        for i in range(len(s)):
            temp = self._max_palindrome(s, i, i)
            if len(temp) > len(res):
                res = temp
        for i in range(1, len(s)):
            temp = self._max_palindrome(s, i- 1, i)
            if len(temp) > len(res):
                res = temp
        return res

    def _max_palindrome(self, s: str, left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]

if __name__ == '__main__':
    s = "ac"
    sol = Solution()
    print(sol.longestPalindrome(s))
