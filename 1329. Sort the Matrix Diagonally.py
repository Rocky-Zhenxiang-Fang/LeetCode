from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Idea:
            1. Get each element in a diagonal and store it in a array1
                Starting from the top or the right, pick each element with [row + 1, col + 1] until the edge
            2. Sort that array
            3. Fill it back
                Starting from the same point, fill back one by one
        """

        def sort_dia(s_r, s_c):
            elements = []
            r, c = s_r, s_c
            while r < len(mat) and c < len(mat[0]):
                elements.append(mat[r][c])
                r += 1
                c += 1
            elements.sort()
            r, c = s_r, s_c
            for e in elements:
                mat[r][c] = e
                r += 1
                c += 1

        if not mat:
            return mat

        for start_row in range(len(mat)):  # upper left is [start_row, 0]
            sort_dia(start_row, 0)
        for start_col in range(1, len(mat[0])):  # [0, 0] is already sorted
            sort_dia(0, start_col)
        return mat


if __name__ == '__main__':
    sol = Solution()
    m = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    print(sol.diagonalSort(m))
