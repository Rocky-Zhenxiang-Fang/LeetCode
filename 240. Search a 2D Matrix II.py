from typing import List


class Solution:
    def searchMatrix_mlogn(self, matrix: List[List[int]], target: int) -> bool:
        """
        Do a binary search on each row
        """
        for i in range(len(matrix)):
            left, right = 0, len(matrix[i]) - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return False

    def searchMatrix_space(self, matrix: List[List[int]], target: int) -> bool:
        """
        Idea:
            Since it is sorted, we can start from the antidiagonal, if smaller then target, move upward, if bigger,
            move right
        """
        if not matrix:
            return False
        row, col = len(matrix) - 1, 0
        while row >= 0 and col < len(matrix[0]):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                col += 1
            else:
                row -= 1
        return False

if __name__ == '__main__':
    mat = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    tar = 5
    mat_2 = [[-1, 3]]
    tar_2 = 3
    sol = Solution()
    print(sol.searchMatrix(mat, tar))
