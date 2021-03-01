class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        """
        Idea:
            The denominator is 8 ** K
            Moves can be store in a list [[2, 1], [1, 2], ..., [-1, -2]], which means the diff in rows and diff in cols
            Brute Force to simulate the problem
            DP to speed up the process
            dp[N][N][K]
        Alg:
            for k in K:
                for row in N:
                    for col in N:
                        if dp[k][row][col]:
                            for each move:
                                if it is not out of bound:
                                    fill in

            return sum(dp[K - 1]) / 8 ** K
        """
        moves = [[2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2], [-2, -1], [-1, -2]]
        dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(K)]
        dp[r][c][0] = 1
        res = 0
        for k in range(K):
            for row in range(N):
                for col in range(N):
                    if dp[k][row][col]:
                        for m in moves:
                            if 0 <= row + m[0] < N and 0 <= col + m[1] < N:
                                if k == K - 1:
                                    res += dp[k][row][col]
                                else:
                                    dp[k + 1][row + m[0]][col + m[1]] += dp[k][row][col]

        return res / 8 ** K


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightProbability(3, 2, 0, 0))
