from typing import List


class Solution:
    # def frequencySort(self, s: str) -> str:
    #     """
    #     slow O(nlogn)
    #     :param s:
    #     :return:
    #     """
    #     res = ""
    #     freqCount = {}
    #     for ch in s:
    #         if ch not in freqCount:
    #             freqCount[ch] = 1
    #         else:
    #             freqCount[ch] = freqCount[ch] + 1
    #     sortedFreqCount = sorted(freqCount.items(), key=lambda d: d[1], reverse=True)
    #     for item, value in sortedFreqCount:
    #         for i in range(value):
    #             res += item
    #     return res
    def frequencySort(self, s: str) -> str:
        import collections
        import heapq
        res = ""
        heap = []
        freqCounter = collections.Counter(s)
        for k, f in freqCounter.items():
            heap.append((-f, k * f))
        heapq.heapify(heap)
        while heap:
            f, ks = heapq.heappop(heap)
            res += ks
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.frequencySort("cccaaa"))

