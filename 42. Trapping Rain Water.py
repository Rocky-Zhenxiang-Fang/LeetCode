from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Insight:
            Q_1: For a column, what is the number of water that this column can store?
            A_1: The difference between its own height and the smallest tallest height from each side
            Let's say that left is the smaller one, as long as left is not increased, answer will always
            be determine by the left height, thus, we want to move the left pointer
        """
        res = 0
        if len(height) < 3:
            return res
        left, right = 0, len(height) - 1
        left_height, right_height = height[left], height[right]

        while left < right:
            left_height = max(left_height, height[left])
            right_height = max(right_height, height[right])
            if left_height <= right_height:
                res += left_height - height[left]
                left += 1
            else:
                res += right_height - height[right]
                right -= 1

        return res


if __name__ == '__main__':
    h = [6, 4, 2, 0, 3, 2, 0, 3, 1, 4, 5, 3, 2, 7, 5, 3, 0, 1, 2, 1, 3, 4, 6, 8, 1, 3]
    sol = Solution()
    print(sol.trap(h))
