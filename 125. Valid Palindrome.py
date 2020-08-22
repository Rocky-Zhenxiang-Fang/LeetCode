class Solution:
    def isPalindrome(self, s: str) -> bool:
        can = ""
        for ch in s:
            if ch.isalpha() or ch.isnumeric():
                can += ch.lower()
        i = 0
        j = len(can) - 1

        while i < j:
            if can[i] is not can[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    s = "0P"
    sol = Solution()
    print(sol.isPalindrome(s))