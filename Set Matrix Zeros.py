class Solution:
    def setZeroes(self, matrix):
        """
        from:
        https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/discuss/806459/Python-Solution-(long-but-intuitive-with-comments)
        """
        rN = len(matrix)
        cN = len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        for i in range(rN):
            if matrix[i][0] == 0:
                first_col_zero = True
                break

        for i in range(cN):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        for row in range(rN):
            for col in range(cN):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, rN):
            for col in range(1, cN):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for i in range(cN):
                matrix[0][i] = 0

        if first_col_zero:
            for j in range(rN):
                matrix[j][0] = 0


if __name__ == '__main__':
    mat = [[1,0,3]]
    sol = Solution()
    sol.setZeroes(mat)
    print(mat)