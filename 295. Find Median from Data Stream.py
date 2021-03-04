import heapq


class MedianFinder:
    """
    Idea:
        Using two heap, one for storing the big half of numbers and the other stores the small half of number
        Assuming that we have n numbers, the small heap should store n // 2 or n // 2 + 1 numbers and big heap should store
        n // 2 numbers. In this case, the median will be either the average of the biggest smaller number and the smallest bigger number
        or the biggest smaller number depending n % 2
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.size = 0  # use to determine the size of two heaps
        self.big_heap = []
        self.small_heap = []
        heapq.heapify(self.big_heap)
        heapq.heapify(self.small_heap)

    def addNum(self, num: int) -> None:
        self.size += 1
        heapq.heappush(self.small_heap, -num)  # always push into the small_heap first, we want to get in reverse order
        if (self.size % 2 == 0 and len(self.small_heap) > self.size // 2) or (
                self.size % 2 == 1 and len(self.small_heap) > self.size // 2 + 1):
            heapq.heappush(self.big_heap, -heapq.heappop(self.small_heap))
        if self.big_heap and self.big_heap[0] < -self.small_heap[0]:  # if this two are not in the right order, swap it
            big = heapq.heappop(self.big_heap)
            small = heapq.heappop(self.small_heap)
            heapq.heappush(self.small_heap, -big)
            heapq.heappush(self.big_heap, -small)

    def findMedian(self) -> float:
        if self.size % 2 == 0:
            return (self.big_heap[0] - self.small_heap[0]) / 2
        return -self.small_heap[0]


if __name__ == '__main__':
    med = MedianFinder()
    med.addNum(1)
    med.addNum(2)
    print(med.findMedian())
    med.addNum(3)
    print(med.findMedian())
    for i in range(4, 10):
        med.addNum(i)
        print(med.findMedian())