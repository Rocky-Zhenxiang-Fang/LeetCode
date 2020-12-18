from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        Idea: Just like two count, record half of the possible values, then see if the other half can match
        """
        numbers = {}
        res = 0
        for a in A:
            for b in B:
                numbers[a + b] = numbers.get(a + b, 0) + 1
        for c in C:
            for d in D:
                if - c - d in numbers:
                    res += numbers[-c - d]
        return res


if __name__ == '__main__':
    sol = Solution()
    A = [1, 2]
    B = [-2, -1]
    C = [-1, 2]
    D = [0, 2]
    print(sol.fourSumCount(A, B, C, D))
