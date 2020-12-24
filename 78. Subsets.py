from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Idea: in each recursive call
            the last item from nums is popped out
            even though one item can be added or not, only the condition that adds the element is importand
        """
        res = []
        visited = set()

        def recur(sub: List[int], remaining: List[int]) -> None:
            if set(sub) not in visited and len(remaining) >= 0:
                visited.add(frozenset(sub))  # record visited set
                res.append(sub)
                for i in range(len(remaining)):
                    recur(sub + [remaining[i]], remaining[:i] + remaining[i + 1:])

        recur([], nums)
        return res



if __name__ == '__main__':
    sol = Solution()
    print(sol.subsets([1, 2, 3]))

