class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        for i in range(len(palindrome) // 2):
            if palindrome[i] != "a":
                return palindrome[:i] + "a" + palindrome[i + 1:]
        return palindrome[:-1] + "b"

if __name__ == '__main__':
    palindrome = "abccba"
    sol = Solution()
    print(sol.breakPalindrome(palindrome))
