from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
        This is a batch sum problem, same thing done in computer vision
        """
        sum_matrix = self.sum_matrix(mat)
        res = []
        for row in range(len(mat)):
            new_row = []
            res.append(new_row)
            for col in range(len(mat[0])):
                top_left = (max(0, row - K), max(0, col - K))
                bottom_right = (min(len(mat) - 1, row + K), min(len(mat[0]) - 1, col + K))
                res[row].append(sum_matrix[bottom_right[0]][bottom_right[1]])
                if top_left[0] > 0:
                    res[row][col] -= sum_matrix[top_left[0] - 1][bottom_right[1]]
                if top_left[1] > 0:
                    res[row][col] -= sum_matrix[bottom_right[0]][top_left[1] - 1]
                if top_left[0] > 0 and top_left[1] > 0:
                    res[row][col] += sum_matrix[top_left[0] - 1][top_left[1] - 1]

        return res

    def sum_matrix(self, mat: List[List[int]]) -> List[List[int]]:
        res = []
        for row in range(len(mat)):
            new_row = []
            for col in range(len(mat[0])):
                new_row.append(mat[row][col])
                if row > 0:
                    new_row[col] += res[row - 1][col]
                if col > 0:
                    new_row[col] += new_row[col - 1]
                if row > 0 and col > 0:
                    new_row[col] -= res[row - 1][col - 1]
            res.append(new_row)
        return res


if __name__ == '__main__':
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    K = 1
    sol = Solution()
    print(sol.matrixBlockSum(mat, K))
