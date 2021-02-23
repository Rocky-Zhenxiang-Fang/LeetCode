from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Idea:
            This is actually a stacked 1D sorted array
            binary search but map 1D pointers to rows can cols
        """
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            r, c = self.id_to_rc(mid, cols)
            if target == matrix[r][c]:
                return True
            elif target < matrix[r][c]:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def id_to_rc(self, index: int, cols: int) -> List[int]:
        return [index // cols, index % cols]


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    sol = Solution()
    print(sol.searchMatrix(matrix, target))
