from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flower = 0
        cannot_place = 0
        placed_flower = 0
        for hole in flowerbed:
            if hole == 1:
                cannot_place = 1
                if placed_flower:
                    max_flower -= 1
                    placed_flower = 0
            else:
                if cannot_place == 1:
                    cannot_place = 0
                    placed_flower = 0
                else:
                    max_flower += 1
                    placed_flower = 1
                    cannot_place = 1
        return max_flower >= n


if __name__ == '__main__':
    sol = Solution()
    test_arr = [1, 0, 0, 0, 1]
    test_n = 2
    print(sol.canPlaceFlowers(test_arr, test_n))
