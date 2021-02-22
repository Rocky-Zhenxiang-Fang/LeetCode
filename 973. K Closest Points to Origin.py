from typing import List


class Solution:
    def kClosest_naive(self, points: List[List[int]], K: int) -> List[List[int]]:
        points.sort(key=lambda x: x[0] ** 2 + x[1] ** 2)
        return points[:K]

    def kClosest(self, points, K):
        self.sort(points, 0, len(points) - 1, K)
        return points[:K]

    def sort(self, points, l, r, K):
        if l < r:
            p = self.partition(points, l, r)
            if p == K:
                return
            elif p < K:
                self.sort(points, p + 1, r, K)
            else:
                self.sort(points, l, p - 1, K)

    def partition(self, points, l, r):
        pivot = points[r]
        a = l
        for i in range(l, r):
            if (points[i][0] ** 2 + points[i][1] ** 2) <= (pivot[0] ** 2 + pivot[1] ** 2):
                points[a], points[i] = points[i], points[a]
                a += 1
        points[a], points[r] = points[r], points[a]
        return a


if __name__ == '__main__':
    points = [[2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [2, 2], [1, 1]]
    K = 1
    sol = Solution()
    print(sol.kClosest(points, K))
