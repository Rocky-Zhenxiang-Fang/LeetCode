from typing import List
import collections


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        Idea:
            Each even node, fill the most frequently seen node, if cannot, fill other
            Then fill odd nodes
        """
        bar_counter = collections.Counter(barcodes)
        res = [0] * len(barcodes)
        max_occur = max(bar_counter.values())
        for k, v in bar_counter.items():
            if v == max_occur:
                max_ele = k
                break
        idx = 0
        for _ in range(bar_counter[max_ele]):
            res[idx] = max_ele
            idx += 2
        # all max_ele has already been stored
        del bar_counter[max_ele]
        for k, v in bar_counter.items():
            for _ in range(v):
                if idx >= len(res):
                    idx = 1
                res[idx] = k
                idx += 2

        return res


if __name__ == '__main__':
    sol = Solution()
    bar = [1, 1, 1, 1, 2, 2, 3, 3]
    print(sol.rearrangeBarcodes(bar))
