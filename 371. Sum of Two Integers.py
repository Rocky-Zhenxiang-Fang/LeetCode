class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        From: https://www.youtube.com/watch?v=qq64FrA2UXQ
        """
        # carry = a & b
        # res = a ^ b
        # while carry:
        #     carry << 1
        #     res = carry ^ res
        #     carry = res & carry
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b), ((a & b) << 1)
        return a


if __name__ == '__main__':
    sol = Solution()
    print(sol.getSum(3, -2))