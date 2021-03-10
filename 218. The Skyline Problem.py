from typing import List
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """
        Idea:
            Do the way that human does
            1. We draw a line from left to right
            2. A critical point is a point where height changes
            3. Height would change at the beginning of the building or the end
            4. The start of the building will always increase the height, the end will always decrease
            5. Height should be monotonic increasing stack since we want to know how much we should lower it when meeting a end
        Alg:
            Put all points in a heap, in form of (index, start or end, height)
            Init height as [0]
            while heap:
                curr = heap.pop()
                if curr is start:
                    update if curr.height > height
                    check if overlapped
                else:
                    update if curr.end < end
        """
        heap = []
        heapq.heapify(heap)
        for b in buildings:
            heapq.heappush(heap, (b[0], "start", b[2]))
            heapq.heappush(heap, (b[1], "end", b[2]))
        res = []
        heights = [0]
        while heap:
            index, is_start, h = heapq.heappop(heap)
            if is_start == "start":
                if h > heights[-1]:
                    while res and res[-1][0] == index:
                        if h > res[-1][1]:
                            res.pop()
                    heights.append(h)
                    res.append([index, heights[-1]])
            else:
                if h < heights[-1]:
                    if res and res[-1][0] == index:
                        if h < res[-1][1]:
                            res.pop()
                    heights.pop()
                    res.append([index, heights[-1]])

        return res


if __name__ == '__main__':
    sol = Solution()
    b = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(sol.getSkyline(b))