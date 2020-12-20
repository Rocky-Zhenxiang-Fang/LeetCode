from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        freq_map = {}
        pq = []
        heapq.heapify(pq)
        res = []
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        for j in freq_map:
            heapq.heappush(pq, (-freq_map[j], j))
        for i in range(k):
            res.append(heapq.heappop(pq)[1])
        return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))

