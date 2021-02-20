from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Idea:
            If a car at behind can reach the target faster then the car ahead, then those cars become a car fleet
        """
        ans = 0
        curr_time = 0
        time = [(target - position[i]) / speed[i] for i in range(len(speed))]
        data = sorted(zip(position, time), key=lambda x: -x[0])
        for d in data:
            if d[1] > curr_time:
                ans += 1
                curr_time = d[1]
        return ans


if __name__ == '__main__':
    sol = Solution()
    t = 12
    pos = [10, 8, 0, 5, 3]
    spe = [2, 4, 1, 1, 3]
    print(sol.carFleet(t, pos, spe))
