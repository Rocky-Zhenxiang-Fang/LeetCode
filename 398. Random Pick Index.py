from typing import List
import random

class Solution:

    def __init__(self, nums: List[int]):
        self.val_index = {}
        for i, v in enumerate(nums):
            self.val_index[v] = self.val_index.get(v, []) + [i]

    def pick(self, target: int) -> int:
        tar = self.val_index[target]
        idx = random.randrange(0, len(tar))
        return tar[idx]
