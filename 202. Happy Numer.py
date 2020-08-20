class Solution:
    def isHappy(self, n: int) -> bool:
        """
        if a number is showed twice, meaning that the loop will go infinitely, return False
        else, return true
        :param n:
        :return:
        """
        sSet = set()
        while n != 1:
            sSet.add(n)
            nStr = str(n)
            nextN = 0
            for ch in nStr:
                nextN += int(ch) ** 2
            if nextN in sSet:
                return False
            else:
                n = nextN
        return True


if __name__ == '__main__':
    inputN = 19
    sol = Solution()
    print(sol.isHappy(inputN))