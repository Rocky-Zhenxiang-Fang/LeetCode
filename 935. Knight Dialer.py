class Solution:
    def knightDialer(self, n: int) -> int:
        neighbor_map = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        dp = [1 for _ in range(10)]
        for row in range(1, n):
            next_dp = [0 for _ in range(10)]
            for col in range(10):
                for nei in neighbor_map[col]:
                    next_dp[col] += dp[nei]
            dp = next_dp
        return sum(dp) % (10**9 + 7)


if __name__ == '__main__':
    sol = Solution()
    print(sol.knightDialer(3131))
