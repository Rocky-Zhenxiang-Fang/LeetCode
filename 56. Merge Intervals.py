from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        from collections import deque
        sortedInt = sorted(intervals, key=lambda x: x[0])
        sortedInt = deque(sortedInt)
        res = []
        while len(sortedInt) >= 2:
            first = sortedInt.popleft()
            second = sortedInt.popleft()
            if first[0] <= second[0] <= first[1]:
                merged = [0, 0]
                merged[0] = min(first[0], second[0])
                merged[1] = max(first[1], second[1])
                sortedInt.appendleft(merged)
            else:
                res.append(first)
                sortedInt.appendleft(second)
        if sortedInt:
            res.append(sortedInt[0])
        return res


if __name__ == '__main__':
    arr = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
    sol = Solution()
    print(sol.merge(arr))
