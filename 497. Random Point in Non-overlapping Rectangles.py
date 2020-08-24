import bisect
import random
from itertools import accumulate
from typing import List


class Solution:

    def __init__(self, rects: List[List[int]]):
        w = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.weights = [item / sum(w) for item in accumulate(w)]
        self.rects = rects

    def pick(self) -> List[int]:
        """
        Uses bisect to find the right rect index

        """
        rectIndex = bisect.bisect(self.weights, random.random())
        tarRect = self.rects[rectIndex]
        return [random.randint(tarRect[0], tarRect[2]), random.randint(tarRect[1], tarRect[3])]

