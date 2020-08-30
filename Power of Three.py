class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        addUp = 0
        nStr = str(n)
        ptr = 0
        if nStr[0] == "-":
            ptr += 1
        while ptr < len(nStr):
            addUp += int(nStr[ptr])
            ptr += 1
        return addUp % 3 == 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPowerOfThree(0))