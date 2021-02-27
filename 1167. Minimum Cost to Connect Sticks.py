from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        """
        Idea:
            The earlier two sticks are merged, the more times them will be added to the sum
            Thus, in every iteration, we want to merge the shortest sticks
        """
        import heapq
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            val1 = heapq.heappop(sticks)
            val2 = heapq.heappop(sticks)
            res += val1 + val2
            heapq.heappush(sticks, val2 + val1)

        return res


if __name__ == '__main__':
    sticks = [2, 4, 3]
    print(sorted(sticks))
    sol = Solution()
    print(sol.connectSticks(sticks))
