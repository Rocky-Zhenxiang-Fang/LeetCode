from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        import collections
        import heapq
        res = []
        ans = []
        words_counter = collections.Counter(words)
        pq = []
        heapq.heapify(pq)
        for w in words_counter:
            heapq.heappush(pq, (-words_counter[w], w))
        for _ in range(k):
            res.append(heapq.heappop(pq))
        res.sort(key=lambda x: (x[0], x[1]))
        for r in res:
            ans.append(r[1])
        return ans


if __name__ == '__main__':
    w = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    k = 4
    sol = Solution()
    print(sol.topKFrequent(w, k))
