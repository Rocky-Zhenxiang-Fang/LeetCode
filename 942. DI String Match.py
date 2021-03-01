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
        left, right = 0, len(S)
        for ch in S:
            if ch == "I":
                res.append(left)
                left += 1
            else:
                res.append(right)
                right -= 1
        return res + [left]


if __name__ == '__main__':
    sol = Solution()
    print(sol.diStringMatch("IDID"))
