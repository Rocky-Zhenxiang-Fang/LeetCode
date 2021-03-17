from typing import List

from DS import TreeNode
import collections


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        included = {}
        left, right = 0, 0
        res = 0
        while right < len(s):
            while len(included) <= k and right < len(s):
                included[s[right]] = included.get(s[right], 0) + 1
                res = max(res, right - left + 1)
                right += 1
            if len(s) <= right:
                break
            while right > left and len(included) > k:
                included[s[left]] -= 1
                if included[s[left]] == 0:
                    del included[s[left]]
                left += 1

        return res


if __name__ == '__main__':
    pass
