class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        ptr = 0
        prev = ""
        while ptr < len(s):
            if prev in map and map[prev] < map[s[ptr]]:
                res += map[s[ptr]] - map[prev]
                prev = ""
            else:
                if prev in map:
                    res += map[prev]
                prev = s[ptr]
            ptr += 1
        if prev != "":
            res += map[prev]
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))