import random
import math
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.origin = [x_center, y_center]

    def randPoint(self) -> List[float]:
        rad = self.r * (random.uniform(0, 1)) ** 0.5
        theta = random.uniform(0, 2 * math.pi)
        x = rad * math.cos(theta) + self.origin[0]
        y = rad * math.sin(theta) + self.origin[1]
        return [x, y]

