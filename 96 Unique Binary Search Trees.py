class Solution:
    def numTrees(self, n: int) -> int:
        """
        The subtree of a BST is also a BST
        If choosing the root as the smallest or the biggest number,
        the problem is numTrees(0) * numTrees(n - 1), (since the other side of tree will have nothing).
        If choosing the second most value, the problem is numTree(1) * numTree(n - 2)
        For example,
        numTree(4) is:
            numTree(0) * numTree(3) +
            numTree(1) * numTree(2) +
            numTree(2) * numTree(1) +
            numTree(3) * numTree(0) +
        So, the problem can be solved using dynamic programming
        """
        dp = [0 for _ in range(n + 1)]
        dp[0], dp[1] = 1, 1
        for i in range(2, len(dp)):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]

        return dp[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.numTrees(4))