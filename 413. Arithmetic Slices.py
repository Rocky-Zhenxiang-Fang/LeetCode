from typing import List


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        """
        Idea:
            First, find the longest non overlapped subarrays that is arithmetic series, then count its number
        Optimal:
            We can do the number counting and searching for subarray in the same round
        Alg:
            left = start of the current subarray
            res = the number to be returned
            dp = [0 for _ in range(len(A))]
            for i in range(len(dp)):
                if A[left:i] is subarray:
                    dp[i] = 2 * dp[i - 1] + 1
                else:
                    update res
                    update left
        """
        if len(A) < 3:
            return 0
        left = 0
        res = 0
        dp = [0 for _ in range(len(A))]
        diff = -1
        for right in range(1, len(dp)):
            if A[right] - A[right - 1] == diff:
                if right - left >= 2:
                    dp[right] = 2 * dp[right - 1] - dp[right - 2] + 1
            else:
                diff = A[right] - A[right - 1]
                left = right - 1
                res += dp[right - 1]
        res += dp[-1]
        return res


if __name__ == '__main__':
    sol = Solution()
    test_1 = [1, 2, 3, 4, 5, 6]
    print(sol.numberOfArithmeticSlices(test_1))


