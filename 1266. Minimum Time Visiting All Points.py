from typing import List


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        """
        Idea: If we can take diagonal step, take it, other wise, take horizontal or vertical steps
        """
        res = 0
        for i in range(1, len(points)):
            past_location = points[i - 1]
            curr_location = points[i]
            x_difference = abs(past_location[0] - curr_location[0])
            y_difference = abs(past_location[1] - curr_location[1])
            res += max(x_difference, y_difference)
        return res


if __name__ == '__main__':
    points = [[1,1],[3,4],[-1,0]]
    sol = Solution()
    print(sol.minTimeToVisitAllPoints(points))

