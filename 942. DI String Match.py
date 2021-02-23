from typing import List


class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        """
        Idea:
            Greedy:
                Leave as much space as possible
                If seeing "I", put the smallest available number
                If seeing "D", put the biggest available number
        """
        res = []
        small, big = 0, len(S)
        for i in range(len(S)):
            if S[i] == "I":
                res.append(small)
                small += 1
            else:
                res.append(big)
                big -= 1
        res.append(small)   # the last element left
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.diStringMatch("IDID"))