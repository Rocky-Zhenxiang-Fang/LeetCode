from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """
        Idea:
            For each element in arr, it is clear that all of them can form a one length tree
            If we want to build a bigger tree, we can two trees and see if the product of their root existed in arr
            The number of Tree will be the product of the number of two subtrees
        """
        arr.sort()
        dp = [1] * len(arr)
        index = {a: i for i, a in enumerate(arr)}
        for i in range(len(arr)):   # target
            for j in range(i):      # left to target
                right = arr[i] / arr[j]
                if right in index:
                    dp[i] += dp[j] * dp[index[right]]
        return sum(dp) % (10 ** 9 + 7)


if __name__ == '__main__':
    sol = Solution()
    arr = [2, 4, 5, 10]
    print(sol.numFactoredBinaryTrees(arr))
