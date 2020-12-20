from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        import heapq
        self.pq = []
        self.max_k = k
        heapq.heapify(self.pq)
        for n in nums:
            if len(self.pq) < k:
                heapq.heappush(self.pq, n)
            else:
                heapq.heappushpop(self.pq, n)

    def add(self, val: int) -> int:
        if len(self.pq) < self.max_k:
            heapq.heappush(self.pq, val)
        else:
            heapq.heappushpop(self.pq, val)
        return self.pq[0]


if __name__ == '__main__':
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3)) # return 4
    print(kthLargest.add(5)) # return 5
    print(kthLargest.add(10))  # return 5
    print(kthLargest.add(9)) # return 8
    print(kthLargest.add(4)) # return 8
