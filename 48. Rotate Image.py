from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        To rotate clockwise, we can frst swap rows, and then transpose the matrix
        """
        if len(matrix) <= 1:
            return
        for i in range(len(matrix) // 2):
            matrix[i], matrix[len(matrix) - 1 - i] = matrix[len(matrix) - 1 - i], matrix[i]

        for row in range(len(matrix)):
            for col in range(row, len(matrix[0])):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]


