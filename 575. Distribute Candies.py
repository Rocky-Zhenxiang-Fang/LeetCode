from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        types = set()
        for c in candyType:
            types.add(c)
        return min(len(candyType) // 2, len(types))


if __name__ == '__main__':
    sol = Solution()
    candies = [1, 1, 2, 2, 3, 3]
    print(sol.distributeCandies(candies))
