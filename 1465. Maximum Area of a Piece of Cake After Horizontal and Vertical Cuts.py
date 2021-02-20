from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        """
        Idea:
            The max area is surrounded by max horizontal difference and vertical difference
        """
        horizontalCuts = [0] + sorted(horizontalCuts) + [h]
        verticalCuts = [0] + sorted(verticalCuts) + [w]
        max_hor, max_ver = -float("inf"), -float("inf")
        for i in range(1, len(horizontalCuts)):
            max_hor = max(max_hor, horizontalCuts[i] - horizontalCuts[i - 1])
        for i in range(1, len(verticalCuts)):
            max_ver = max(max_ver, verticalCuts[i] - verticalCuts[i - 1])
        return (max_hor * max_ver) % (10 ** 9 + 7)

if __name__ == '__main__':
    sol = Solution()
    h = 5
    w = 4
    horizontalCuts = [1, 2, 4]
    verticalCuts = [1, 3]
    print(sol.maxArea(h, w, horizontalCuts, verticalCuts))


