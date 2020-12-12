from typing import List
import heapq


class KthLargest:
    """
    Idea: only stores the elements that is bigger then kth element.
     If a new element is added, if it is smaller then the current kth element, discard it since it will never show up
     if it is bigger, add it into heap, remove the smallest one
    """

    def __init__(self, k: int, nums: List[int]):
        self.top_k_values = []
        self.k = k
        heapq.heapify(self.top_k_values)
        nums.sort(reverse=True)
        for i in range(min(k, len(nums))):
            heapq.heappush(self.top_k_values, nums[i])

    def add(self, val: int) -> int:
        kth_smallest = -float("inf")
        if len(self.top_k_values) >= self.k:
            kth_smallest = heapq.heappop(self.top_k_values)
        heapq.heappush(self.top_k_values, max(kth_smallest, val))
        return self.top_k_values[0]
