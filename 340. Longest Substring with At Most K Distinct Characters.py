class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        visited = {}
        included = 0
        left, right = 0, 0
        res = 0
        while right < len(s):
            if s[right] not in visited or visited[s[right]] == 0:
                included += 1
            visited[s[right]] = visited.get(s[right], 0) + 1
            if included <= k:
                res = max(res, right - left + 1)
            else:
                while left < right and included > k:
                    visited[s[left]] -= 1
                    if visited[s[left]] == 0:
                        included -= 1
                    left += 1

            right += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    s = "aba"
    k = 1
    print(sol.lengthOfLongestSubstringKDistinct(s, k))