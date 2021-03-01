from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        """
        Idea:
            Possible candidates are from [1,...,6] and needs to be at each pair of A, B
        Alg:
            Try if all dices can be A[0] or B[0], if can, return the min cost, if cannot, return - 1
        """

        def flip(target) -> int:
            a_cost, b_cost = 0, 0
            for i in range(len(A)):
                if A[i] != target and B[i] != target:
                    return float("inf")
                elif A[i] != target and B[i] == target:
                    a_cost += 1
                elif B[i] != target and A[i] == target:
                    b_cost += 1
            return min(a_cost, b_cost)

        return min(flip(A[0]), flip(B[0])) if flip(A[0]) != float("inf") or flip(B[0]) != float("inf") else -1


if __name__ == '__main__':
    sol = Solution()
    A = [2, 1, 2, 4, 2, 2]
    B = [5, 2, 6, 2, 3, 2]
    print(sol.minDominoRotations(A, B))
