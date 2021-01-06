from typing import List


class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        lights = [0 for _ in range(len(bulbs))]
        for i in range(len(bulbs)):
            lights[bulbs[i] - 1] = 1
            if self.is_valid(lights, k):
                return i + 1
        return -1

    def is_valid(self, lights, k) -> bool:
        counter = -1
        for l in lights:
            if l == 1:
                if counter == k:
                    return True
                counter = 0
            else:
                if counter >= 0:
                    counter += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    bulbs = [1,3,2]
    k = 1
    print(sol.kEmptySlots(bulbs, k))