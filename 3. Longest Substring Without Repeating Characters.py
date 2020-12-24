class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        included = set()
        start, end = 0, 0
        while start < len(s):
            if s[start] not in included:
                included.add(s[start])
                start += 1
            else:
                max_length = max(max_length, start - end)
                while s[start] in included:
                    included.remove(s[end])
                    end += 1
        return max(max_length, start - end)


if __name__ == '__main__':
    sol = Solution()
    test = " "
    print(sol.lengthOfLongestSubstring(test))
