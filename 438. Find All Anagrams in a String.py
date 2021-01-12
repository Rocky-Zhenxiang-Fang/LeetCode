from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Idea:
            Sliding window, if a char belongs to p is added, the difference between the two -1, and vice versa
        """
        from collections import Counter
        if not s or not p or len(p) > len(s):
            return []
        difference = len(p)
        res = []
        p_counter = Counter(p)
        s_counter = {}
        left, right = 0, 0
        while right < len(s):
            s_counter[s[right]] = s_counter.get(s[right], 0) + 1
            if s[right] in p_counter and s_counter[s[right]] <= p_counter[s[right]]:
                difference -= 1
            else:
                difference += 1
            if right - left >= len(p):
                if s[left] in p_counter and s_counter[s[left]] <= p_counter[s[left]]:
                    difference += 1
                else:
                    difference -= 1
                s_counter[s[left]] -= 1
                left += 1
            right += 1
            if difference == 0:
                res.append(left)
        return res


if __name__ == '__main__':
    sol = Solution()
    test1s = "cbaebabacd"
    test1p = "abc"
    print(sol.findAnagrams(test1s, test1p))







