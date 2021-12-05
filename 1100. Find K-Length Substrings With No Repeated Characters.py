class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        from collections import Counter
        start_counter = Counter(s[:k])
        right = k
        res = 1 if len(start_counter) == k else 0
        while right < len(s):
            start_counter[s[right - k]] -= 1
            if start_counter[s[right - k]] == 0:
                del start_counter[s[right - k]]
            start_counter[s[right]] += 1
            if len(start_counter) == k:
                res += 1
            right += 1
        return res


if __name__ == "__main__":
    sol = Solution()
    s = "havefunonleetcode"
    print(sol.numKLenSubstrNoRepeats(s, 5))