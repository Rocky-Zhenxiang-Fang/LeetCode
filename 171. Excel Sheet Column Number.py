class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for ch in columnTitle:
            res = res * 26 + (ord(ch) - ord("A") + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("A"))