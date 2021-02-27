from DS import TreeNode

class Solution:
    def getMoneyAmount(self, n):
        need = [[0] * (n + 1) for _ in range(n + 1)]
        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                                   for x in range(lo, hi))
        return need[1][n]


if __name__ == '__main__':
    for i in range(1, 20):
        sol = Solution()
        print(str(i) + ":" + str(sol.getMoneyAmount(i)))
