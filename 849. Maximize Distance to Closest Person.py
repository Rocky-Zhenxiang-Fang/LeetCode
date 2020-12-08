from typing import List

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        """
        two pointers
        previous: points to the previous taken seat
        i: current pointer while looping
        three cases:
        normal case: pick up the seat in the middle of previous taken seat and current taken seat to achieve biggest distance
        edge case 1: first seat is 0, in this way the largest distance is between position 0 and the first taken seat, since you can
        take the target seat at position 0
        edge case 2: last seat is 0, in this way the largest distance is between the previous taken seat and the last position,
        because you can place the target seat at the last position
        """

        result = 0
        previous = -1  # initiate the previous taken seat to last position
        n = len(seats)
        for i in range(n):
            if seats[i]:  # if seats at i is taken
                if previous == -1:  # i is the first seat ever met
                    result = i  # this take care of the edge case 1 when position 0 is not taken
                else:
                    # normal case:
                    result = max(result, (i - previous) // 2)
                # update the most recent taken seat
                previous = i
        # at last, check the edge case 2
        result = max(result, n - previous - 1)
        return result


if __name__ == '__main__':
    sol = Solution()
    s = [1,0,0,0,1,0,1]
    print(sol.maxDistToClosest(s))