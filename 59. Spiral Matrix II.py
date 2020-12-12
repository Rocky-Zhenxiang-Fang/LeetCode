from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0 for _ in range(n)] for _ in range(n)]
        direction = [0, 1]  # row, col
        current = [0, 0]
        for i in range(1, n ** 2 + 1):
            result[current[0]][current[1]] = i
            if result[(current[0] + direction[0]) % n][(current[1] + direction[1]) % n]:
                direction[0], direction[1] = direction[1], -direction[0]
            current[0] += direction[0]
            current[1] += direction[1]
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.generateMatrix(3))
