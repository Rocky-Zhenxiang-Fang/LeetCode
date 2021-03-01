from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr_copy = arr[:]
        duped = 0
        i = 0
        while i < len(arr):
            val = arr_copy[i + duped]
            arr[i] = val
            if val == 0 and i != len(arr) - 1:
                arr[i + 1] = 0
                i += 1
                duped += 1

