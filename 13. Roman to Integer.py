class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Idea, since if the right char is bigger then the left char, the left char will turn to negative, we can
        analyze from the right, in this case, we don't need to deal with two digit at once.
        """
        converter = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        ptr = len(s) - 1
        while ptr >= 0:
            if ptr != len(s) - 1 and converter[s[ptr + 1]] > converter[s[ptr]]:
                res -= converter[s[ptr]]
            else:
                res += converter[s[ptr]]
            ptr -= 1
        return res


if __name__ == '__main__':
    s = "III"
    sol = Solution()
    print(sol.romanToInt(s))