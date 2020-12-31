# This file is used to review done questions

# Definition for a binary tree node.
from typing import List, Set

import DS


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Idea: if two interval can be merged, the bigger start must be in between the smaller start and smaller end
            Thus, we can first sort intervals by the start point, and check if intervals can be merged
            If cannot be merged, add the interval into the res
        """
        res = []
        intervals.sort(key=lambda x: x[0])
        start, end = intervals[0][0], intervals[0][1]
        for i in intervals:
            if start <= i[0] <= end:
                end = max(end, i[1])
            else:
                res.append([start, end])
                start, end = i[0], i[1]
        res.append([start, end])
        return res


if __name__ == '__main__':
    intervals = [[2,6], [1,3],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(intervals))
