import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) >= 2:
            a = -heapq.heappop(stones)
            b = -heapq.heappop(stones)
            if a != b:
                heapq.heappush(stones, -abs(a - b))

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]


if __name__ == '__main__':
    sol = Solution()
    arr = [2, 7, 4, 1, 8, 1]
    print(sol.lastStoneWeight(arr))
