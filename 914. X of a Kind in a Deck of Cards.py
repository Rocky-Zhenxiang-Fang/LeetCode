from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        Idea:
            Find is there a common division across all occurrence
        """
        from collections import Counter
        occur = Counter(deck)
        for k, v in occur.items():
            if v < 2:
                return False
        sor = sorted(v for k, v in occur.items())
        can = self.find_divisons(sor[0])
        for c in can:
            flag = True
            for i in range(1, len(sor)):
                if sor[i] % c != 0:
                    flag = False
            if flag:
                return flag
        return False

    def find_divisons(self, s: int):
        res = [s]
        upper = s ** 0.5
        i = 2
        while i <= upper:
            if s % i == 0:
                res.append(i)
                res.append(s // i)
            i += 1
        return res


if __name__ == '__main__':
    deck = [1, 1, 1, 2, 2, 2, 3, 3]
    sol = Solution()
    print(sol.hasGroupsSizeX(deck))
