from typing import List
import collections


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if difference == 0:
            return max(collections.Counter(arr).values())
        dp = {}
        for a in arr:
            if a not in dp:
                dp[a] = 1
            if a - difference in dp:
                dp[a] = max(dp[a], dp[a - difference] + 1)
        
        return max(dp.values())


if __name__ == '__main__':
    sol = Solution()
    arr = [3,0,-3,4,-4,7,6]
    diff = 3
    print(sol.longestSubsequence(arr, diff))