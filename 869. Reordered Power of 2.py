from typing import Set, List
import collections


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """
        Idea:
            If a number is a permutation of an other number, this means that these two numbers has same digit counts
            For all possible 2 candidates, check if it has the same digit to N
        """
        counter = collections.Counter(str(N))
        twos = [2 ** i for i in range(31)]
        res = 0
        for t in twos:
            if collections.Counter(str(t)) == counter:
                res += 1
        return res == 1


if __name__ == '__main__':
    sol = Solution()
    test = 46
    print(sol.reorderedPowerOf2(test))