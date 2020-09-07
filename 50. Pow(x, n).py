class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        From https://ithelp.ithome.com.tw/articles/10214426
        Using recurssion to solve the problem
        Main idea: x ** 2y = x ** y * x ** y
                   x ** (2y + 1) = (x ** y) * (x ** y) * x
        """
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            return half * half
        elif n > 0:
            return half * half * x
        else:
            return half * half / x


if __name__ == "__main__":
    sol = Solution()
    print(sol.myPow(2.000, n = -2))