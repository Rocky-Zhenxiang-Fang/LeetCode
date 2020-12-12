from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        left, right = 0, len(height) - 1
        while left < right:
            result = max(result, (right - left) * min(height[right], height[left]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result