class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return self._isPalindrome(s, left + 1, right) or self._isPalindrome(s, left, right - 1)

        return True

    def _isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True
