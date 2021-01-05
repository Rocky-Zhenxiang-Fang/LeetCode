from typing import List


class Solution:
    def numSubmat_brute_force(self, mat: List[List[int]]) -> int:
        """
        Brute Force Solution:
            For each element = 1, search for all its submatrix
        """
        self.count = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    self._helper(row, col, mat)

        return self.count

    def _helper(self, row, col, mat):
        """
        given the upper left corner, extend right once at a time until it is 0. In each extend, also try to extend down
        """
        bound = len(mat)
        for right in range(col, len(mat[0])):
            if mat[row][right] == 0:
                break
            for down in range(row, bound):
                if mat[down][right] == 1:
                    self.count += 1
                else:
                    bound = down
                    break
        return

    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        # precipitate mat to histogram
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0:
                    mat[i][j] += mat[i - 1][j]  # histogram

        ans = 0
        for i in range(m):
            stack = []  # mono-stack of indices of non-decreasing height
            cnt = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]:
                    jj = stack.pop()  # start
                    kk = stack[-1] if stack else -1  # end
                    cnt -= (mat[i][jj] - mat[i][j]) * (jj - kk)  # adjust to reflect lower height

                cnt += mat[i][j]  # count submatrices bottom-right at (i, j)
                ans += cnt
                stack.append(j)

        return ans


if __name__ == '__main__':
    mat = [[0,1,1,0],[0,1,1,1],[1,1,1,0], [0, 1, 1, 1]]
    sol = Solution()
    print(sol.numSubmat(mat))
