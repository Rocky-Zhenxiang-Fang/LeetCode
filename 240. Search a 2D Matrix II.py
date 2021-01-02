from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Idea: pick rows that might contain the target, then do binary search
        """

        if not len(matrix) or not len(matrix[0]):
            # Quick response for empty matrix
            return False
        h, w = len(matrix), len(matrix[0])
        for row in matrix:
            # range check
            if row[0] <= target <= row[-1]:
                # launch binary search on current possible row
                left, right = 0, w - 1
                while left <= right:
                    mid = left + (right - left) // 2
                    mid_value = row[mid]
                    if target > mid_value:
                        left = mid + 1
                    elif target < mid_value:
                        right = mid - 1
                    else:
                        return True
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
    print(sol.searchMatrix(mat_2, tar_2))
