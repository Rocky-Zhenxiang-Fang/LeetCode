from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Idea:
            First define a direction, if the direction is not valid, change according right, down, left, up
            DFS:
                mark visited cell as -10000 since this number will never exist
        """
        res = []
        stack = [(0, 0)]
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        rows, cols = len(matrix), len(matrix[0])
        while stack:
            curr = stack.pop()
            res.append(matrix[curr[0]][curr[1]])
            if len(res) == rows * cols:
                break
            matrix[curr[0]][curr[1]] = - 10000
            while True:
                m = moves[direction]
                nr, nc = curr[0] + m[0], curr[1] + m[1]
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] != -10000:
                    stack.append((nr, nc))
                    break
                else:
                    direction = (direction + 1) % 4
        return res


if __name__ == '__main__':
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print((sol.spiralOrder(mat)))
