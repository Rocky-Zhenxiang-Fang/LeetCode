from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        top_right = [min(rec1[2], rec2[2]), min(rec1[3], rec2[3])]
        lower_left = [max(rec1[0], rec2[0]), max(rec1[1], rec2[1])]
        return top_right[0] > lower_left[0] and top_right[1] > lower_left[1]


