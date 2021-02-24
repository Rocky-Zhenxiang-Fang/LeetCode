from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Idea:
            Sort intervals by start, this ensures that we don't need to revisit intervals
            Two intervals can be merged if range1[0] <= range2[0] <= range1[1]
        """
        intervals.sort(key=lambda x: x[0])
        stack = []
        for i in intervals:
            while stack:
                prev = stack.pop()
                if prev[0] <= i[0] <= prev[1]:
                    i = [prev[0], max(prev[1], i[1])]
                else:
                    stack.append(prev)
                    break
            stack.append(i)

        return stack


if __name__ == '__main__':
    arr = [[1,3],[2,6],[8,10],[15,18]]
    sol = Solution()
    print(sol.merge(arr))
