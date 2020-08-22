class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        import math
        if num == 0:
            return False
        m = math.log(num, 4)
        return int(m) == m


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfFour(16))