from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.left_up_sum = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.left_up_sum[row][col] += matrix[row][col]
                if row > 0: self.left_up_sum[row][col] += self.left_up_sum[row - 1][col]
                if col > 0: self.left_up_sum[row][col] += self.left_up_sum[row][col - 1]
                if row > 0 and col > 0: self.left_up_sum[row][col] -= self.left_up_sum[row - 1][col - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.left_up_sum[row2][col2]
        if row1 > 0: res -= self.left_up_sum[row1 - 1][col2]
        if col1 > 0: res -= self.left_up_sum[row2][col1 - 1]
        if row1 > 0 and col1 > 0: res += self.left_up_sum[row1 - 1][col1 - 1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
