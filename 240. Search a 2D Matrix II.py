class Solution:
    def searchMatrixMine(self, matrix, target):  # Takes too much memory
        check = set()

        def dfs(r, c) -> bool:
            if (r, c) in check or r == -1 or r == len(matrix) or c == -1 or c == len(matrix[0]):
                return False
            else:
                check.add((r, c))
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                return dfs(r + 1, c) or dfs(r, c + 1)
            else:
                return dfs(r - 1, c) or dfs(r, c - 1)

        row = len(matrix) // 2
        col = len(matrix[0]) // 2
        return dfs(row, col)

    def searchMatrix(self, matrix, target):
        for row in matrix:
            col = len(matrix[0]) - 1
            while col != 0 and row[col] > target:
                col -= 1
            else:
                if row[col] == target:
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
    sol = Solution()
    print(sol.searchMatrix(mat, tar))
