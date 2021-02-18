from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Idea:
            Brute Force: try all possibility. O(n^2)
            Optimal:
                Observe:
                    The volume is dominated by the lower bound. Thus, we want to move the lower bound
                Solution:
                    Two pointer
        """
        res = 0
        left, right = 0, len(height) - 1
        while left <= right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res
