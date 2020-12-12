import collections
from typing import List
import heapq


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    #     """
    #     idea: add all elements in the sliding window into a PQ with (value, index), in each iteration
    #     see if the next element in the PQ is in the sliding window, if not, remove it and do it again
    #     if so, put the value into res
    #     """
    #     start = 0   # the first element in the sliding window
    #     res = []
    #     priority_que = []
    #     heapq.heapify(priority_que)
    #     for i in range(k - 1):  # fill up the PQ
    #         heapq.heappush(priority_que, (-nums[i], i)) # negative for the max heap
    #     while start + k <= len(nums):
    #         heapq.heappush(priority_que, (-nums[start + k - 1], start + k - 1))
    #         candidate = priority_que[0]  # peaking the "biggest" element
    #         while candidate[1] < start:  # index of the value in nums is not in the sliding window
    #             heapq.heappop(priority_que)  # remove this item
    #             candidate = priority_que[0]
    #         res.append(-candidate[0])
    #         start += 1
    #
    #     return res

    def maxSlidingWindow(self, nums, k):
        """
        From https://leetcode.com/problems/sliding-window-maximum/discuss/65901/9-lines-Ruby-11-lines-Python-O(n)
        Keep indexes of good candidates in deque d. The indexes in d are from the current window, they're increasing,
        and their corresponding nums are decreasing. Then the first deque element is the index of the largest window
        value.
        For each index i:
        Pop (from the end) indexes of smaller elements (they'll be useless).
        Append the current index.
        Pop (from the front) the index i - k, if it's still in the deque (it falls out of the window).
        If our window has reached size k, append the current window maximum to the output.
        """
        d = collections.deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()
            d += i,
            if d[0] == i - k:
                d.popleft()
            if i >= k - 1:
                out += nums[d[0]],
        return out


if __name__ == '__main__':
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))



