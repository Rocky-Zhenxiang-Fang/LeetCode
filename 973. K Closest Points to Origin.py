from typing import List


class Solution:
    def kClosest_naive(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Idea:
            Do quick select
            In each iteration, after partition,
                If K == pivot location, return. Since the first K element will be the answer
                If K > pivot location, keep partition the right side since we need more
                If K < pivot location, partition the left side since some of those unordered element is useless
        """
        self.quick_select(points, K, 0, len(points) - 1)
        return points[:K]

    def quick_select(self, points: List[List[int]], K: int, left: int, right: int) -> None:
        while left <= right:
            pivot = self.partition(points, left, right)
            if pivot == K:
                return
            elif pivot < K:
                left = pivot + 1
            else:
                right = pivot - 1

    def partition(self, points: List[List[int]], left: int, right: int) -> int:
        pivot = points[left]
        small = left + 1
        big = right
        while True:
            while small < big and self.dis(points[small]) <= self.dis(pivot):
                small += 1
            while small <= big and self.dis(points[big]) >= self.dis(pivot):
                big -= 1
            if small >= big: break
            points[small], points[big] = points[big], points[small]
        points[left], points[big] = points[big], points[left]
        return big

    def dis(self, p):
        return p[0] ** 2 + p[1] ** 2


if __name__ == '__main__':
    p = [[-5, 4], [-3, 2], [0, 1], [-3, 7], [-2, 0], [-4, -6], [0, -5]]
    k = 6
    sol = Solution()
    print(sol.kClosest(p, k))
