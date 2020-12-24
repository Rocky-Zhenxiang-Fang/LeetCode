from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], day: int) -> int:
        """
        From: https://www.youtube.com/watch?v=CoNBRq5JSz0
        Idea: the min capacity of the ship is max(weights), the ship should be able to ship the heaviest item
              the max capacity of the shop is sum(weights), the ship can ship all item at once
              To find if any capacity in (min_capa, max_capa), do a greedy to separate items then count the day
              use binary search to update min, max
        """
        min_capacity = max(weights)
        max_capacity = sum(weights)
        while min_capacity <= max_capacity:
            mid = (min_capacity + max_capacity) // 2
            d = 1   # number of days needed
            ship_load = 0   # the load of the current ship
            for i in weights:
                if ship_load + i <= mid:
                    ship_load += i
                else:
                    d += 1
                    ship_load = i
            if d > day:    # needed more day to ship the items
                min_capacity = mid + 1
            else:                   # the capacity could be lower
                max_capacity = mid - 1
        return min_capacity


if __name__ == '__main__':
    sol = Solution()
    weights = [3,2,2,4,1,4]
    D = 3
    print(sol.shipWithinDays(weights, D))
