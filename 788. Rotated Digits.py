class Solution:
    def rotatedDigits_brute_force(self, N: int) -> int:
        """
        If a number has 3, 4, 7, this means that this number is invalid
        If a number does not have 2, 5, 6, 9, it is also invalid
        """
        from collections import Counter
        res = 0
        for n in range(1, N + 1):
            counter = Counter(list(str(n)))
            if "3" in counter or "4" in counter or "7" in counter:
                continue
            if "2" not in counter and "5" not in counter and "6" not in counter and "9" not in counter:
                continue
            res += 1
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.rotatedDigits_brute_force(10))
