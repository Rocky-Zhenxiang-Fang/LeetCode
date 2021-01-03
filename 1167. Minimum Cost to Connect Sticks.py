from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        import heapq
        pq = []
        res = 0
        heapq.heapify(pq)
        for s in sticks:
            heapq.heappush(pq, s)
        while len(pq) > 1:
            item_1 = heapq.heappop(pq)
            item_2 = heapq.heappop(pq)
            res += item_2 + item_1
            heapq.heappush(pq, item_1 + item_2)
        return res


if __name__ == '__main__':
    sticks = [2,4,3]
    print(sorted(sticks))
    sol = Solution()
    print(sol.connectSticks(sticks))
