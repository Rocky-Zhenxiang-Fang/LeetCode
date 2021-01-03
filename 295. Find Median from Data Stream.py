class MedianFinder:
    """
    Idea: since we only need to find the median, we only need to make sure the middle two element
        We can have two heap, one stores the first half and the other stores the second half
    """

    def __init__(self):
        """
        initialize your data structure here.
        big always keep the bigger half of elements and pop the smallest among them
        small always keep the smaller half of the elements and pop the biggest among them
        """
        import heapq
        self.big = []
        self.small = []
        heapq.heapify(self.big)
        heapq.heapify(self.small)

    def addNum(self, num: int) -> None:
        """
        When adding a number, we first determine if ti belongs to the first half or the second half
        After this, we need to make sure that both pq does not have length difference bigger then 1
        """
        import heapq
        if self.big and  num > self.big[0]:   # if num is bigger then the smallest element of the bigger half
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -num)

        # check size
        if len(self.big) > len(self.small) + 1:     # big is longer by small by more then 1
            mid = heapq.heappop(self.big)   # pop the smallest item in big
            heapq.heappush(self.small, -mid)    # add it into the smaller half
        elif len(self.small) > len(self.big) + 1:
            mid = heapq.heappop(self.small)   # pop the biggest item in small
            heapq.heappush(self.big, -mid)    # add it into the bigger half

    def findMedian(self) -> float:
        if len(self.big) == len(self.small):    # even situation
            return (self.big[0] - self.small[0]) / 2
        elif len(self.big) > len(self.small):
            return self.big[0]
        else:
            return -self.small[0]