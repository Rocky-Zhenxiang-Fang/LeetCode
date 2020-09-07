class Solution:
    def titleToNumber(self, s: str) -> int:
        mapping = {}
        for i in range(65, 91):
            mapping[chr(i)] = i - 64
        res = 0
        for ch in s:
            res = res * 26 + mapping[ch]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.titleToNumber("A"))