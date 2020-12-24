from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Idea:
        For each recursive call, check if target is smaller then zero and if the target, sub combination have been seen
        if not, subtract the target by each element of target, and pass the same remaining
        """
        res = []

        def recur(sub: List[int], remaining: List[int], tar) -> None:
            if tar >= 0 and len(remaining) >= 0:
                if tar == 0:
                    res.append(sub)
                else:
                    for i in range(len(remaining)):
                        recur(sub + [remaining[i]], remaining[i:], tar - remaining[i])
        recur([], candidates, target)
        return res


if __name__ == '__main__':
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(sol.combinationSum(candidates, target))
