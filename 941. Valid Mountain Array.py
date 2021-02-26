from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        start, end = 0, len(arr) - 1
        for start in range(len(arr) - 1):
            if arr[start] >= arr[start + 1]:
                break
        for end in range(len(arr) - 1, 0, -1):
            if arr[end] >= arr[end - 1]:
                break
        return start == end and start != 0 and end != len(arr) - 1

